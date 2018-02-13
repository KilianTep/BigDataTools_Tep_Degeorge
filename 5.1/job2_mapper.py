#!/usr/bin/python
import sys
import string

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    #separates word_id and count
    word_id, count = line.split('\t',1)
    	
    #separates word from id
    word, doc= word_id.split('@',1)
    print ('%s\t%s%s%s' % (doc, word,'=',count))