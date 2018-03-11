Exercise 5.1 for Celine Hudelot's class: Big Data Algorithms
TF-IDF ranking of two provided texts in repos
Hadoop: 2.8.2
Python: 3.6.3

Run on terminal (on macOS):
$ sh tf_idf.sh

- Job1:
Map:
  Input: (document, each line contents)
  Output: (word@document, 1))
Reducer
  n = sum of the values of for each key “word@document”
  Output: ((word@document), n)

- Job2:
Map:
  Input: ((word@document), n)
  Re-arrange the mapper to have the key based on each document
  Output: (document, word=n)
Reducer
  N = totalWordsInDoc = sum [word=n]) for each document
  Output: ((word@document), (n/N))

- Job 3:
Map:
  Input: ((term@document), n/N)
  Re-arrange the mapper to have the word as the key, since we need to count the number of documents where it occurs
  Output: (term, document=n/N)
Reducer:
  D = total number of documents in corpus. This can be passed by the driver as a constant;
  d = number of documents in corpus where the term appears. It is a counter over the reduced values for each term;
  TFIDF = n/N * log(D/d);
  Output: ((word@document), d/D, (n/N), TFIDF)
  
  - Sorting job:
  Last file, which uses pandas Dataframe for sorting.
  Prints the top 20 words with highest TF-IDF scores.

Source: https://marcellodesales.wordpress.com/2009/12/31/tf-idf-in-hadoop-part-1-word-frequency-in-doc/
