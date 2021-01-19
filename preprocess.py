import sys
import json
import os
from os import path

END = '_end_'
PATH = os.getcwd() + '/trie'
DATASET_FOLDER = sys.argv[1]


class db:
    def __init__(self):
        self.gen_db()

    # Generate your trie
    def gen_db(self):
        files = os.listdir(DATASET_FOLDER)

        # Uncomment this line to test on small number of files
        # files = files[:2]
        for file in files:
            self.parse(file)

    # Parse through emails
    def parse(self, file):
        words = []
        with open(DATASET_FOLDER + "/" + file, "r") as dataFile:
            for line in dataFile:
                for word in line.split():
                    words.append(word)

        index = ''.join(file.split())[:-4]
        trie = self.make_trie(words, index)
        self.list_words(trie, PATH)

    # Make tries for each mail
    def make_trie(self, words, index):
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[END] = index
        return root

    # Create folders when recursing through the trie
    def list_words(self, trie, dir):
        my_list = []

        # Reached end
        if (isinstance(trie, str)):
            name = dir + "/node.txt"

            # Node.txt already exists
            if path.isfile(name):
                with open(name, "a+") as dataFile:
                    for line in dataFile:
                        if line == trie:
                            return []
                    dataFile.write(" " + trie)
                return []
            else:
                # Node.txt does not exist
                with open(os.path.join(dir, "node.txt"), 'w') as f:
                    for index in trie:
                        f.write(index)
                return []

        # Recurse through trie
        for k, v in trie.items():
            if k != '_':
                folder = dir
                try:
                    folder += "/" + k
                    os.mkdir(folder)
                except OSError as error:
                    pass

                for el in self.list_words(v, folder):
                    my_list.append(k + el)
            else:
                my_list.append('')
        return my_list


db = db()
