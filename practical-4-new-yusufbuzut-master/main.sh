#!/bin/bash

#### Q1 #### 

cat htmls.txt | sed -E 's/^\s*<\s*(\w*)\s*.*\s*>\s*.*/\1/'
#### Q2 #### 
cat htmls.txt | sed -E 's/^\s*<\s*\w*\s*.*\s*>\s*(\w*)\s*<\s*.*.*/\1/'

#### Q3 #### 
cat words.txt | grep ".*a.*a.*a.*"

#### Q4 #### 
cat words.txt | grep ".*a.*a.*a.*" | grep -v ".*'s" | sed -E 's/.*(..)/\1/' | sort | uniq -c | sort -nk1,1 | tail -n1 | awk '{print $2}'
#### Q5 #### 

cat ssh_log.txt | sed -E 's/^Invalid\s*\w*\s*\w*\s*\w*\s*(\w*)\s*at\s*.*\s*.*\s*.*/\1/' | sort | uniq -c | sort -nk1,1 | tail -n5 
#### Q6 #### 
cat ssh_log.txt | sed -E 's/^Blocked\s*\w*\s*\w*\s*\w*\s*(\w*)\s*at\s*.*\s*.*\s*.*/\1/' | sort | uniq -c | sort -nk1,1 | tail -n5 
#### Q7 #### 

cat ssh_log.txt | sed -E 's/^\s*\w*\s*\w*\s*\w*\s*\w*\s*(\w*)\s*at\s*.*\s*.*\s*.*/\1/' | sort | uniq -c | sort -nk1,1 | tail -n5 



