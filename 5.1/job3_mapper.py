#!/usr/bin/python
import sys
import string

# Job3: Map:
# Input: ((term@document), n/N)
# Re-arrange the mapper to have the word as the key, since we need to count the number of documents where it occurs
# Output: (term, document=n/N)

for line in sys.stdin:
	   # remove leading and trailing whitespace
    line = line.strip()

    #separates the word from its doc and frequency
    word, doc_frequency = line.split('@',1)

    #separates doc_frequency above in doc and frequency
    doc, frequency = doc_frequency.split('\t',1)

    print ('%s\t%s%s%s' % (word, doc,'=',frequency))