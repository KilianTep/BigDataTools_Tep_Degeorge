#!/usr/bin/python
import sys
import string

#Input: FromNodeId \t 1.0_<All ToNodeIds>
#Output: ToNodeId A \t (PageRank / TotalOutLinks)
#        FromNode B \t <All ToNodeIds> 
#We are putting A,B as distinct markers we will reuse in the reducer

# input comes from STDIN (standard input)
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    #split the line into Arrival Node and 1.0_<All ToNodeIds>
    FromNodeId, PR_outlinks = line.split('\t',1)

    #separate page rank(PR) from arrival nodes
    PR, outlinks = PR_outlinks.split('_')

    try:
      PR = float(PR)
    except ValueError:
        continue

    ToNodeIdList = outlinks.split(' ')

    TotalOutLinks = len(ToNodeIdList)

    if TotalOutLinks != 0:
        for ToNodeId in ToNodeIdList:
            ToNodeIdA = ToNodeId + ' A'
            print('%s\t%s'%(ToNodeIdA, PR/TotalOutLinks))
        FromNodeIdB = FromNodeId + ' B'
        print('%s\t%s' % (FromNodeIdB,outlinks))
