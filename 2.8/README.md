### 2.8
We will work with the file isd-history.txt of the NOAA. This file is available here : https://www1. ncdc.noaa.gov/pub/data/noaa/isd-history.txt. \
Put it on HDFS and then use the command hdfs -dfs - tail file to see this last lines. Your job is to write a program using the HDFS API that will display the USAF code, the name, the country (FIPS country ID) and the elevation of each station. \
Some important points : \
— The first 22 lines of the file have to be ignored (they do not contain data). \
— The name of each station begins at the character 13 of a line and its size is 29 characters long. — The FIPS begins at the character 43 of a line and its size is 2 characters long.\
— The altitude begins at the character 74 of a line and its size is 7 characters long.
