#!/bin/bash

# define three variables: max_run, unwanted, and unwanted_count
# take the first two as the first two arguments, respectively
# initialize the unwanted_counter to 0

max_run=$1
unwanted=$2
unwanted_count=0


# in a for loop from 1 to max_run
for i in $(seq 1 $max_run); do
  # echo iteration number
  echo $i

  # run mystic with the unwanted number as the argument
  ./mystic.sh $unwanted

  # check the return code of the previous command
  # increment unwanted_counter if there is an error
  if [[ $? -ne 0 ]]; then
    unwanted_count=$((unwanted_count+1))
  fi
  
done

echo "In $max_run runs, the number of encounters with the unwanted number $unwanted is $unwanted_count."
