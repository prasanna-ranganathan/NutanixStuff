#!/bin/bash

sum_third_feilds() {
    sum=0
    while IFS=: read -r name shawdow uid gid uidinfo homedir command
    do
           sum=$(( sum + uid ))
    done < "$file"

    echo "Total Sum for the Third Feild Value is: $sum"
}

if [ "$#" -ne 1 ]; then
   echo "Usage: ./Script.sh /etc/passwd"
   exit 1
else
   file=$1
   if [ ! -f "$file" ]; then
      echo "File Not Found!"
      exit 1
   fi
   sum_third_feilds $file
fi
