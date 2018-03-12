#!bin/bash
# This shell is to run exercice 5.2: Page Rank of Epinion Graph
# Here we are assuming that the shell cd is the main one/highest level in the computer so Hadoop Streaming Jar file, 
# the input text have to be in this cd. We are also assuming you use hadoop-streaming-2.8.2.jar
# we are also assuming that hadoop has been started
#

echo "Copy the soc-Epinions1 file from local to input folder"
hdfs dfs -rm -r -f /page_rank/
hdfs dfs -mkdir /page_rank
hdfs dfs -mkdir /page_rank/input
hdfs dfs -copyFromLocal soc-Epinions1.txt /page_rank/input

echo "Run the initializer"
hadoop jar hadoop-streaming-2.8.2.jar -D mapred.reduce.tasks=0 -mapper "python pr_initializer.py" -reducer "python pr_reducer.py"   -input /page_rank/input/* -output /page_rank/output1

echo "Run the MapReduce 15 times"

for ((i=1; i<15; i++)); do

	j=$[$i+1]
	hadoop jar hadoop-streaming-2.8.2.jar  -mapper "python pr_mapper.py" -reducer "python pr_reducer.py"   -input /page_rank/output$i/* -output /page_rank/output$j

	echo "iteration number $i complete"
done

echo "Run the mapper with a last reducer so we get only Final PR_score"
hadoop jar hadoop-streaming-2.8.2.jar  -mapper "python pr_mapper.py" -reducer "python pr_reducer_last.py"   -input /page_rank/output15/* -output /page_rank/last_output

echo "Sorting of the Top 10 page ranks"
hadoop jar hadoop-streaming-2.8.2.jar -D mapred.reduce.tasks=0 -mapper "python pr_sorter.py" -reducer "python pr_reducer.py"   -input /page_rank/last_output/* -output /page_rank/sorted_page_rank

echo "The nodes with the top 10 page ranks are:"
hdfs dfs -cat /page_rank/sorted_page_rank/*