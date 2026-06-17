import unittest
from datetime import date

import pandas as pd

from scripts import augment_raw_data as ard


class TestAugmentFunctions(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "poet": ["Living Poet", "Multi Poet", "Multi Poet", "Posthumous Poet"],
            "poem": ["A", "B", "C", "D"],
            "birth_date": [date(1980, 1, 1), date(1980, 1, 2), date(1980, 1, 2), date(1920, 1, 3)],
            "death_date": [pd.NaT, pd.NaT, pd.NaT, date(2010, 1, 3)],
            "pub_date": [date(2000, 1, 1), date(2000, 1, 2), date(2010, 1, 2), date(2025, 1, 3)]
        })
        self.date_columns = ["birth_date", "death_date", "pub_date"]

    def tearDown(self):
        del self.df
        del self.date_columns

    def test_extract_decade(self):
        dt = date(1819, 5, 31)
        self.assertEqual(ard.extract_decade(dt), 1810)

    def test_extract_decade_null(self):
        self.assertIsNone(ard.extract_decade(pd.NaT))

    def test_nth_ring(self):
        row = self.df.iloc[0]
        self.assertEqual(ard.nth_ring(row, "pub_date"), 3)

    def test_nth_ring_posthumous(self):
        row = self.df.iloc[-1]
        self.assertEqual(ard.nth_ring(row, "death_date"), 10)
        self.assertEqual(ard.nth_ring(row, "pub_date"), 11)

    def test_nth_ring_null(self):
        row = self.df.iloc[1]
        self.assertIsNone(ard.nth_ring(row, "death_date"))

    def test_day_of_decade(self):
        dt = date(1819, 5, 31)
        self.assertEqual(ard.day_of_decade(dt), 3438)

    def test_day_of_decade_null(self):
        self.assertIsNone(ard.day_of_decade(pd.NaT))

    def test_degree_of_decade(self):
        dt = date(2000, 1, 1)
        self.assertEqual(ard.degree_of_decade(dt), 0)

        dt = date(2009, 12, 31)
        self.assertEqual(round(ard.degree_of_decade(dt)), 360)

    def test_degree_of_decade_three_leap_years(self):
        # The decade 2000 has 3 leap years, 2010 has 2. Thus, the
        # same date will correspond to different degrees.
        dt_a = date(2000, 3, 1)
        dt_b = date(2010, 3, 1)

        self.assertNotEqual(
            ard.degree_of_decade(dt_a),
            ard.degree_of_decade(dt_b)
        )

    def test_degree_of_decade_null(self):
        self.assertIsNone(ard.degree_of_decade(pd.NaT))

    def test_rings_per_poet(self):
        gb = ard.rings_per_poet(self.df)
        self.assertEqual(gb["Living Poet"], 5)

    def test_rings_per_poet_multi(self):
        gb = ard.rings_per_poet(self.df)
        self.assertEqual(gb["Multi Poet"], 5)

    def test_rings_per_poet_posthumous(self):
        gb = ard.rings_per_poet(self.df)
        self.assertEqual(gb["Posthumous Poet"], 11)


if __name__ == "__main__":
    unittest.main()
