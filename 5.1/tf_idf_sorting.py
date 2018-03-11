#!/usr/bin/python
import sys
# coding: utf-8
import pandas as pd

col_names = ["doc@id", "d/D", "TF", "TF_IDF"]
TFIDF_DF = pd.DataFrame(columns=col_names)

for line in sys.stdin:

	line = line.strip()

	DocAtId, d_D, TF, TF_IDF = line.split('\t')
	TF_IDF = float(TF_IDF)

	TFIDF_DF = TFIDF_DF.append({'doc@id': DocAtId, 'd/D':d_D,'TF':TF,'TF_IDF':TF_IDF},ignore_index=True)

TFIDF_DF = TFIDF_DF.sort_values(by='TF_IDF',ascending=False)
TFIDF_DF =TFIDF_DF.reset_index(drop=True)

#prints top 20 TF_IDF words
print(TFIDF_DF[0:20])

