#!/usr/bin/env python
from operator import itemgetter
import sys
import numpy as np

#number of times that the key appears in corpus
num_key_appears_in_doc = 0

#number of documents in corpus where the term appears.
num_of_doc_in_corpus = 2
IDF = 0
current_word = None
doc_tf = {}

#meant to save the title of doc for checking
#doc_storage = []

#this for_loop iterates over all lines to count the number of documents
for line in sys.stdin:
    #separates word from the rest
    word, doc_frequency = line.split('\t',1)

    #separates doc from frequency
    doc, frequency = doc_frequency.split('=',1)

    #if doc not in doc_storage:
    #    doc_storage.append(doc)


    #stores the number of doc in corpus
    #num_of_doc_in_corpus = len(doc_storage)

        # convert count (currently a string) to int
    try:
        frequency = float(frequency)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue


    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word==word:
        num_key_appears_in_doc += 1
        doc_tf.update({doc:frequency})
    else:
        if current_word:
            IDF = np.log(num_of_doc_in_corpus/num_key_appears_in_doc)
            for document,freq in doc_tf.items():
                if num_key_appears_in_doc != num_of_doc_in_corpus:
                    print('%s%s%s\t%s%s%s\t%s\t%s' %(current_word,'@',document,num_key_appears_in_doc,'/',num_of_doc_in_corpus,freq,freq*IDF))
                else:
                    print('%s%s%s\t%s%s%s\t%s\t%s' %(current_word,'@',document,num_key_appears_in_doc,'/',num_of_doc_in_corpus,freq,freq))
            num_key_appears_in_doc = 0
            doc_tf={}
        current_word=word
        doc_tf.update({doc:frequency})
        num_key_appears_in_doc += 1

#computes the last line if we need to
if current_word == word:
    IDF = np.log(num_of_doc_in_corpus/num_key_appears_in_doc)
    for document,freq in doc_tf.items():
        if num_key_appears_in_doc != num_of_doc_in_corpus:
            print('%s%s%s\t%s%s%s\t%s\t%s' %(current_word,'@',document,num_key_appears_in_doc,'/',num_of_doc_in_corpus,freq,freq*IDF))
        else:
            print('%s%s%s\t%s%s%s\t%s\t%s' %(current_word,'@',document,num_key_appears_in_doc,'/',num_of_doc_in_corpus,freq,freq))