#!/usr/bin/python
import sys
import pandas as pd

col_names = ['NodeId','Page_Rank']
PR_DF = pd.DataFrame(columns=col_names)

for line in sys.stdin:

	NodeId, PR = line.split("\t")
	PR = float(PR)

	PR_DF = PR_DF.append({'NodeId': NodeId,'Page_Rank':PR},ignore_index=True)

PR_DF = PR_DF.sort_values(by='Page_Rank',ascending=False)
PR_DF = PR_DF.reset_index(drop=True)

#print the 10 highest page ranks
print(PR_DF[0:10])