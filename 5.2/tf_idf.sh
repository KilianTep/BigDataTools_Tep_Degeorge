#!bin/bash
# This shell is to run exercice 5.1: TF-IDF of 2 texts in repo
# Here we are assuming that the shell cd is the main one/highest level in the computer so Hadoop Streaming Jar file, 
# the input texts have to be in this cd. We are also assuming you use hadoop-streaming-2.8.2.jar
# we are also assuming that hadoop has been started

echo "Copy the 2 text files from local to input folder"
hdfs dfs -rm -r -f /tf-idf/
hdfs dfs -mkdir /tf-idf
hdfs dfs -mkdir /tf-idf/input
hdfs dfs -copyFromLocal callwild /tf-idf/input
hdfs dfs -copyFromLocal defoe-robinson-103.txt /tf-idf/input

echo "Run the First Job of TF-IDF map reduce Job"
hadoop jar hadoop-streaming-2.8.2.jar -mapper "python job1_mapper.py" -reducer "python job1_reducer.py" -input /tf-idf/input/* -output /tf-idf/output_job1

echo "Run the Second Job of TF-IDF map reduce job"
hadoop jar hadoop-streaming-2.8.2.jar -mapper "python job2_mapper.py" -reducer "python job2_reducer.py" -input /tf-idf/output_job1/* -output /tf-idf/output_job2

echo "Run the Third Job of TF-IDF map reduce job"
hadoop jar hadoop-streaming-2.8.2.jar -mapper "python job3_mapper.py" -reducer "python job3_reducer.py" -input /tf-idf/output_job2/* -output /tf-idf/output_job3

echo "Sorting of words with biggest TF-IDF scores"
hadoop jar hadoop-streaming-2.8.2.jar -D mapred.reduce.tasks=0 -mapper "python tf_idf_sorting.py" -reducer "python job3_reducer.py" -input /tf-idf/output_job3/* -output /tf-idf/sorted_output

echo "The top 20 words with the biggest TF-IDF scores are:"
hdfs dfs -cat /tf-idf/sorted_output/*
