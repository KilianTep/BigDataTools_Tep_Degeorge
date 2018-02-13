#!/usr/bin/python
import sys
import string
from nltk.corpus import stopwords
import os

# Map:
# Input: (document, each line contents)
# Output: (word@document, 1))

#removes the most common words of the English language i.e "the", "is","etc"
stopWords = set(stopwords.words('english'))

#lookup table for punctuation
table = str.maketrans({key: None for key in string.punctuation})

#stores the path of file into a string
file_name = os.environ['mapreduce_map_input_file']

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    for word in words:
        #turns word into lower case
        word = word.lower()
        #removes punctuation
        word = word.translate(table)

        if word not in stopWords:
            word = word + "@" + file_name
            print ('%s\t%s' % (word, 1))
