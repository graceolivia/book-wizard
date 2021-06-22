# book-wizard
A command line application that allows you to use the Google Books API to search for books and construct a reading list.

# To run the wizard

1. Clone repo
2. run "source bin/activate"
3. install dependencies with `pipenv install --dev`
4. run `python3 wizard.py`

# To run the tests

After completing steps 1-3 above, run `python3 -m unittest tests.py` to run all tests.

You can also run individual tests with the following command structures:
`python3 -m unittest [module].[class].[test name]`
So, for example, to run only test_yes_or_no_y test in the YesNo class, you would use:
`python3 -m unittest tests.YesNo.test_yn_y`


# Notes

This calls the Google Books API and gives the searcher a list of 5 books to choose from. She can select a book to add to her reading list, view her reading list, make a new query, or quit. The program has 3 main menu options that are available at the beginning of the program's loop, and again when the user finishes with a search. These are to view the reading list, to search, and to quit.

As of this version, the reading list does not persist after the program closes. 

When the user is selecting with a number, her input is checked and she is prompted to correct it if not a valid number. If the Google Books API doesn't return any results, she is also prompted to try a different search.