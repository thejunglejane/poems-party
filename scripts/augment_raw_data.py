"""Augment poets' birth, death, and publication data for visualization.

These data will be visualized as a series of concentric rings
corresponding to decades, similar to tree rings. This script extracts
the decades of a poet's life (and beyond, for posthumously-published
poets) and calculates the degrees within each decade that correspond
to their birth, death, and the publication of their poem(s).
"""
import math
from datetime import date

import pandas as pd


def extract_year(dt):
    if pd.notnull(dt):
        return int(dt.year)


def extract_decade(dt):
    if pd.notnull(dt):
        return int((dt.year // 10) * 10)


def nth_ring(row, column):
    if pd.notnull(row[column]):
        decade = extract_decade(row[column])

        return math.ceil((decade - row["birth_decade"] + 1) / 10)


def day_of_decade(dt):
    if pd.notnull(dt):
        decade = extract_decade(dt)
        decade_begin = date(decade, 1, 1)

        return dt - decade_begin


def degree_of_decade(dt):
    if pd.notnull(dt):
        decade = extract_decade(dt)
        td = day_of_decade(dt)

        # If the first year of a decade is a leap year, it will have
        # 3 leap years (rather than 2). At the granularity/scale of
        # this visualization, 1d doesn't make a noticeable difference.
        denom = 3652
        if decade % 4 == 0:
            denom = 3653

            # Every 100 years we skip a leap year,
            # unless that year is divisible by 400
            if decade % 100 == 0:
                if decade % 400 != 0:
                    denom = 3652

        theta = 360/denom

        return round(td.days * theta, 1)


def rings_per_poet(df):
    df_ = df.copy()

    # Fill in death date information for living poets
    df_["death_date"] = df_["death_date"].fillna(date(2025, 12, 31))
    df_["death_ring"] = df_.apply(lambda x: nth_ring(x, "death_date"), axis=1)

    return df_.groupby("poet")[["death_ring", "pub_ring"]].max().max(axis=1)


# Read in the raw data
df = pd.read_csv("data/poets_poems_raw.csv")
date_columns = ["birth_date", "death_date", "pub_date"]

# Preserve original date information
for column in date_columns:
    df.rename(
        columns={column: "_".join([column, "raw"])},
        inplace=True
    )

# Coerce birth, death, and pub dates to date objects
# format="mixed" to handle Richard Siken, Carolyn Kizer
for column in date_columns:
    df[column] = pd.to_datetime(
        df[f"{column}_raw"],
        errors="coerce",
        format="mixed"
    ).dt.date

# Special case: Python can't parse "Oct/Nov 1963"
df.loc[df["poet"] == "Carolyn Kizer", "pub_date"] = date(1963, 1, 1)


# Extract year, decade, and day of decade from all dates, and determine
# which ring and how many degrees on that ring each date corresponds to
for column in date_columns:
    df[column.replace("date", "year")] = df[column].apply(lambda x: extract_year(x))
    df[column.replace("date", "decade")] = df[column].apply(lambda x: extract_decade(x))
    df[column.replace("date", "day_of_decade")] = df[column].apply(lambda x: day_of_decade(x))
    df[column.replace("date", "ring")] = df.apply(lambda x: nth_ring(x, column), axis=1)
    df[column.replace("date", "degrees")] = df[column].apply(lambda x: degree_of_decade(x))

    # Since we only know Richard Siken's birth year, we treat it as a
    # duration (year) rather than a point in time
    if column == "birth_date":
        df.loc[df["poet"] == "Richard Siken", "birth_degrees_end"] = df["birth_degrees"] + 36

    # Publication is a span (year) rather than a point in time (date),
    # so we capture the ending degree, too
    if column == "pub_date":
        df["pub_degrees_end"] = df["pub_degrees"] + 36


# For living poets, capture their ongoing life from the end
# of the dataset to now
df.loc[df["death_date"].isnull(), "ongoing_begin_degrees"] = degree_of_decade(date(2025, 12, 31))
df.loc[df["death_date"].isnull(), "ongoing_end_degrees"] = degree_of_decade(date.today())


# Determine the total number of rings needed for each poet,
# including posthumously-published poets
gb = rings_per_poet(df)
df["n_rings_total"] = gb[df.set_index("poet").index].values

# Sort the dataset and write to csv
df = df.sort_values(by=["birth_date", "pub_date", "poem"])
df.to_csv("data/poets_poems.csv", index=False, mode="w")
