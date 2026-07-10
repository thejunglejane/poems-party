# The Poems Party

This repository contains [data](https://github.com/thejunglejane/poems-party/tree/main/data) about the poems recited at The Poems Parties (2025). It also contains the [scripts](https://github.com/thejunglejane/poems-party/tree/main/scripts) I used to clean and augment the data for visualization. Both the raw and augmented data are available in CSV format, encoded in UTF-8.

# Methodology

Often, individual poems are first published in magazines and then later published in collections. This dataset aims to capture the original publication date for all poems, the date that represents when the poem first appeared in the world.

This isn't as straightforward as it might seem. Poems can be published and then revised and published again, as is the case with anything in Walt Whitman's *Leaves of Grass*. From 1855 until his death in 1892, Whitman was writing, revising, and expanding the collection. There are [scholarly articles](https://www.proquest.com/openview/18317a6e015cfd89356206111c1c3003/1) dedicated to the question of how many editions of *Leaves of Grass* there are. For Whitman's poem "Crossing Brooklyn Ferry", I chose the earliest instance of that poem *under that name* (though the 1881 version was the one actually recited at The Poems Party II).

Then there's the case of Emily Dickinson, whose poems weren't published in unedited form until 1955 but did appear in the world earlier (albeit edited). I chose the edited publication date.

Finally, there's W. B. Yeats's "Easter, 1916" which was first issued in 1916 as a private printing of 25 copies before being published, several years later, in the New Statesman. I did not consider the private printing "in the world", in contrast to Philip Larkin's pamphlet *XX Poems* which was also printed privately (and later published as *The Less Deceived*) but that he mailed to literary critics and authors.

I've included notes wherever there was ambiguity or I had to make an editorial choice.

## Sources

These data were created by me with the assistance of my sister, p. hodges adams, using sources including: [Wikipedia](wikipedia.org), [Poetry Foundation](poetryfoundation.org), [Poetry Archive](poetryarchive.org), [Pome](https://mattogle.com/#), our personal poetry collections, and the poetry sections at [McNally Jackson](https://mcnallyjackson.com/store/5) and [Daedalus](https://www.instagram.com/daedalusbookscharlottesville/).

During this project, I was surprised by how many poems appear on the internet with incomplete or no citation information. I've included a [works cited](https://github.com/thejunglejane/poems-party/tree/main/data/WORKS_CITED.md) page containing references for publication date information. Some works cited are for the published poems themselves, while others are for material that answer the question "when was this first published?" For collections that I own, there's no electronic container information included. For any collections I don't own, there's an electronic container that shows where I confirmed 1) that a poem was included in the given collection, and 2) the publication information of the collection.

## Corrections

If you find errors in the data, especially earler publications than are captured here, please [open an issue](https://github.com/thejunglejane/poems-party/issues/new/choose) with the correction and a source (cited in MLA format).
