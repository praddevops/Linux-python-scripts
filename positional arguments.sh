#!/bin/sh

#sample shell scripts that takes two numbers as positional arguments and prints their sum

if [ "$#" -ne 2 ]; then
 echo "USAGE: ($0 number1 number2) pass 2 numbers to get their sum"
 exit 1
fi



val=`expr $1 + $2`
echo "sum is $val"
