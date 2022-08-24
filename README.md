# Bible flashcard maker

Simple script that produces `cards.txt` by querying https://labs.bible.org/ api to get a selection of verses.  This file can then be made into Anki cards using [Lyrics/poetry cloze generator](https://ankiweb.net/shared/info/2084557901) or directly into cards via the import function of anki.

Note that if using the built-in anki import, the cards will be formatted as follows:
1. Front: Book Chapter:Verse
2. Back: verse text

Note also that the text produced uses the NET translation