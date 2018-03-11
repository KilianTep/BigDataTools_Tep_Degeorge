Exercise 5.2 for Celine Hudelot's class: Big Data Algorithms
PageRank implementation of Directed Graph (Soc Epinions)
Hadoop: 2.8.2
Python: 3.6.3

Run on terminal (on macOS):
$ sh page_rank.sh

- Initialization:
Input: FromNodeId \t ToNodeId
Ouput: FromNodeId \t 1.0_<All ToNodeIds>

- Mapper
Input: FromNodeId \t 1.0_<All ToNodeIds>
Output: ToNodeId A \t (PageRank / TotalOutLinks)
        FromNode B \t <All ToNodeIds> 
We are putting A,B as distinct markers we will reuse in the reducer

- Reducer (to be run 15 times for convergence)
Input: Sorted by Value: 
		NodeId A \t PageRank / TotalOutLinks
    NodeId B \t <All ToNodeIds> 
Ouput: NodeId\t Page_Rank_<All ToNodeIds>

- Last Reducer (for formatting purposes)
Input: Sorted by Value: 
  NodeId A \t PageRank / TotalOutLinks
  NodeId B \t <All ToNodeIds> 
Ouput: NodeId\t Page_Rank

- Sorting: 
Print the nodes with the top 10 largest Page_Rank Scores
