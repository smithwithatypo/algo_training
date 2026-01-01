
# Algorithm training  

Daily warmups for SWE interview prep sessions  
Inspired by classical music training

## How To Use

1. Open your terminal
1. Install the dependencies  
    - `pip install -r requirements.txt`
1. Run one of the Terminal Commands from the next section
1. Open `warmup.py`
1. Code your solution
1. Hit the Enter key in your original terminal window and repeat from step 3

## Terminal Commands

- Random  
`python3 main.py`

- Pick a WARMUP or EXERCISE from below (shown here is `binary_search`)  
`python3 main.py binary_search`

- Select multiple repetitions (shown here is 5 repetitions)  
`python3 main.py binary_search 5`

## Warmups

1. contains_duplicate
1. count
1. valid_anagram
1. prefix_sum
1. binary_search

## Exercises

(( under construction ))
- binary_search
- oop_basics
- sliding_window
- contains_duplicate
- min_heap
- max_heap
- two_pointers
- sort_inplace_vs_copy
- count_using_hashmap
- count_alphabet_bucket_sort
- list_comprehension
- recursion
- quick_sort
- merge_sort
- linked_list
- tree_bfs
- tree_dfs
- graph_bfs
- graph_dfs
- dfs_directions
- dfs_base_cases
- stack
- prefix_sum
- queue
- greedy
- dynamic_programming

## (optional) Quickstart automation for MacOS or Linux

1. Copy/paste the function below into your .zshrc file and restart your terminal  
2. Then type `warmup` in your terminal to do a problem in VS Code  
  - or `warmup binary_search` to do once
  - or `warmup 5` to do 5 reps of a random warmup
  - or `warmup binary_search 5` to do 5 reps of binary_search
  
``` Bash
warmup() {
    cd /Users/dude/projects/python/algo-training
    if [ $# -eq 0 ]; then
        code warmup.py test_output.log
        python3 main.py
    elif [ $# -eq 1 ]; then
        code warmup.py test_output.log
        python3 main.py "$1"
    else
        code warmup.py test_output.log
        python3 main.py "$1" "$2"
    fi
}
```
