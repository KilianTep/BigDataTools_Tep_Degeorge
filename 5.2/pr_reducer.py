#!/usr/bin/python
import sys

#Input: Sorted by Value: 
#		NodeId A \t PageRank / TotalOutLinks
#       NodeId B \t <All ToNodeIds> 
#Ouput: NodeId\t Page_Rank_<All ToNodeIds>
current_NodeId = None
d = 0.85
Page_Rank = None
outlinks = None

for line in sys.stdin:

	# remove leading and trailing whitespac
	line = line.strip()

	NodeId, Marker_Rest = line.split(" ",1)

	Marker, Rest = Marker_Rest.split("\t",1)

	# 	   # this IF-switch only works because Hadoop sorts map output
#     # by key (here: word) before it is passed to the reducer

	if Marker=='A': #if Marker == A, Rest is equal to PR/TotalOutLinks
		PR_score = float(Rest)
		if current_NodeId==NodeId:
			Page_Rank += d*PR_score
		else:
			# Page_Rank = None 
			current_NodeId = NodeId
			Page_Rank = (1-d) + d*PR_score
	else: #elif Marker=='B' #Marker=='B' indicates the end of loop / Rest corresponds to All ToNodeIds
		outlinks = Rest
		print('%s\t%s%s%s' % (NodeId,Page_Rank,'_',outlinks))
		Page_Rank = None #resets Page Rank for new node
		current_NodeId = None #resets for new Node
