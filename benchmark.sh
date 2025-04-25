#!/bin/bash

# ==============================================================================
# Project Title: Async vs Thread Scraping
# Description: Focuses on comparing the efficiency of different methods for making requests.
# Author: Jishnu S G
# GitHub Repository: https://github.com/jishnukoliyadan/Async-vs-Thread-Scraping
# License: MIT
# ==============================================================================

# Initialize/clear the benchmark result file
> benchmark_result.txt

# Set the PYTHONPATH to the project root directory
export PYTHONPATH=$(pwd)

# If no argument is passed, default to 5 passes, otherwise use the passed value
if [ -z "$1" ]; then
    num_passes=5
else
    num_passes=$1
fi

# Function to run the scraper scripts and benchmark their performance
run_scraper(){
    script_name=$1

    # Log the script name and start the benchmark
    echo "Executing $script_name.py"
    echo -e "$script_name.py\n---------------" >> benchmark_result.txt

    total_time=0

    # Run the scraper script 'num_passes' times
    for i in $(seq 1 "$num_passes")
    do
        # Run the script and capture the last line of the output (which should contain the time taken)
        result=$(uv run "scraper/$script_name.py" | tail -n 1)
        time_taken=$(echo "$result" | awk -F " : " '{print $2}')
        
        # Accumulate the time taken across all passes
        total_time=$(echo "$total_time + $time_taken" | bc -l)
        
        # Output the time for the current pass
        echo "Pass $i/$num_passes : $time_taken"
        
        # Log the result to the benchmark file
        echo $result >> benchmark_result.txt
    done

    # Calculate the average time
    average_time=$(echo "$total_time / $num_passes" | bc -l)

    # Log the average time to the benchmark file
    echo -e "Average time took : $average_time\n" >> benchmark_result.txt
    echo "" # Print a blank line for readability
}


# Run the scrapers: sync, thread, and async
run_scraper "sync_scraper"
run_scraper "thread_scraper"
run_scraper "async_scraper"

# Finally, run a script to process the result images
uv run utils/result_images.py
