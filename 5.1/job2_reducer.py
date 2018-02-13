#!/usr/bin/env python
from operator import itemgetter
import sys


# Job2 Reducer
# N = totalWordsInDoc = sum [word=n]) for each document
# Output: ((word@document), (n/N))

current_doc = None
TotalCount = 0
#storage is meant to be as followed storage[doc_id] = {word:count}. It's a dictionary of dictionary
storage = {}

#inside_dic is will contain the {word:count} of storage[doc_id]
inside_dic = {}

#will store the totalcount of each document ID
TotalCountStorage = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from job2_mapper.py
    doc, word_count = line.split('\t', 1)
    word, count = word_count.split('=',1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_doc == doc:
        TotalCount += count
        inside_dic.update({word:count})
        storage[current_doc] = inside_dic
        TotalCountStorage[current_doc] = TotalCount
    else:
        TotalCount = count
        current_doc = doc
        inside_dic = {word: count}
        storage[current_doc] = inside_dic
        TotalCountStorage[current_doc] = TotalCount

#prints the output on stdout
for doc in storage.keys():
    for word,count in storage[doc].items():
        print('%s%s%s\t%s' % (word,'@',doc, count/TotalCountStorage[doc]))

