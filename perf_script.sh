#!/bin/bash

total_time=0

for i in {1..10}; do
    exec_time=$( { time -p python my_flow.py; } 2>&1 | grep real | awk '{print $2}' )
    echo "Execution time: $exec_time seconds"
    total_time=$(echo "$total_time + $exec_time" | bc -l)
done

average_time=$(echo "scale=3; $total_time / 10" | bc -l)
echo "Average execution time over 10 runs: $average_time seconds"