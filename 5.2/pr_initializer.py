#!/usr/bin/python
import sys

#Input: FromNodeId \t ToNodeId
#Ouput: FromNodeId \t 1.0_<All ToNodeIds>

current_FromNodeId = None
# input comes from STDIN (standard input)
for line in sys.stdin:
    #description of dataset starts with '#''
    #we do not want to treat the data if it starts with '#''
    if line[0] is not '#':

    # remove leading and trailing whitespace
        line = line.strip()
    # split the line into separate departure node and arrival Node
        FromNodeId, ToNodeId= line.split('\t')
   
        # this IF-switch only works because initial dataset
        # is already well sorted
        if current_FromNodeId==FromNodeId:
            #appends to the list of outward nodes if not done 
            #with iterating over list
            out_links += ' ' + ToNodeId
        else:
            if current_FromNodeId:
                print('%s\t%s%s%s' % (current_FromNodeId,'0.5','_',out_links))
            #initiliaze new current_FromNodeId with newly encountered FromNodeId
            current_FromNodeId = FromNodeId
            out_links = ToNodeId
          
if current_FromNodeId == FromNodeId:
    print('%s\t%s%s%s' % (current_FromNodeId,'0.5','_',out_links))






