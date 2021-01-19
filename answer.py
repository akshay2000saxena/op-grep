import os
import json
import sys

DB_JSON = sys.argv[1]
SEARCH_WORD = sys.argv[2]
FILE_NAME = "/_end_/node.txt"


def find(search):

    # Recurse to end of folders just by adding / in the search word
    dir = DB_JSON

    for char in search:
        dir += "/" + char

    dir += FILE_NAME

    # Check if file exists at the end
    try:
        with open(dir) as f:
            print(' '.join(f.readlines()))
    except IOError:
        print("No emails contain the word " + SEARCH_WORD)


# Find
find(SEARCH_WORD)
