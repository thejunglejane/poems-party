# The Poems Party

This repository contains [data](https://github.com/thejunglejane/poems-party/tree/main/data) about the poems recited at The Poems Parties (2025). It also contains the [scripts](https://github.com/thejunglejane/poems-party/tree/main/scripts) I used to clean and augment the data for visualization. Both the raw and augmented data are available in CSV format, encoded in UTF-8.

# Methodology

Often, individual poems are first published in magazines and then later published in collections. This dataset aims to capture the original publication date for all poems, the date that represents when the poem first appeared in the world.

This isn't as straightforward as it might seem. Poems can be published and then revised and published again, as is the case with anything in Walt Whitman's *Leaves of Grass*. From 1855 until his death in 1892, Whitman was writing, revising, and expanding the collection. There are [scholarly articles](https://www.proquest.com/openview/18317a6e015cfd89356206111c1c3003/1) dedicated to the question of how many editions of *Leaves of Grass* there are. For Whitman's poem "Crossing Brooklyn Ferry", I chose the earliest instance of that poem *under that name*. In a similar vein, Michael Ondaatje's poem "The Cinnamon Peeler" first appeared in his fictionalized memoir *Running in the Family*, but that version is different enough from the version my friend recited that I chose the later publication.

Then there's the case of Emily Dickinson, whose poems weren't published in unedited form until 1955 but did appear in the world earlier (albeit edited). I chose the edited publication date.

Finally, there's W. B. Yeats's "Easter, 1916" which was first issued as a private printing of 25 copies before being included, several years later, in his collection *Michael Robartes and the Dancer* ([source](https://en.wikipedia.org/wiki/Easter,_1916)). I did not consider this "in the world", in contrast to Philip Larkin's pamphlet *XX Poems* which was also printed privately (and later published as *The Less Deceived*) but that he mailed to literary critics and authors ([source](https://en.wikipedia.org/wiki/The_Less_Deceived)).

I've included notes wherever there was ambiguity or I had to make an editorial choice.

## Sources

These data were created by me with the assistance of my sister, p. hodges adams, using sources including: [Wikipedia](wikipedia.org), [Poetry Foundation](poetryfoundation.org), [Poetry Archive](poetryarchive.org), [Pome](https://mattogle.com/#), our personal poetry collections, and the poetry sections at [McNally Jackson](https://mcnallyjackson.com/store/5) and [Daedalus](https://www.instagram.com/daedalusbookscharlottesville/).

During this project, I was surprised by how many poems appear on the internet with incomplete or no citation information. In the future, I'll include full citations for the editions/versions that correspond to the publication dates represented in this dataset (see [#1 Add bibliography](https://github.com/thejunglejane/poems-party/issues/1)).
