
# Algorithm training  

Daily warmups for SWE interview prep sessions  
Inspired by classical music training

## How To Use

1. Open your terminal
2. Run one of the Terminal Commands from the next section
3. Open `warmup.py`
4. Code up your solution
5. Hit "Enter" in your original terminal window and repeat from step 3

## Terminal Commands

- Random  
`python3 main.py`

- Pick a WARMUP or EXERCISE from below (shown here is `binary_search`)  
`python3 main.py binary_search`

- Pick one for multiple repetitions  
`python3 main.py binary_search 5`

## Warmups

- binary_search
- two_pointers
- sliding_window
- count
- tree_dfs
- recursion
- linked_list
- stack

## Exercises

- ( under construction )
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

## Quickstart automation

1. Copy/paste the function below into your .zshrc file and restart your terminal  
2. Then type `warmup` or `warmup binary_search 1` in your terminal to do a problem in VS Code  
  - tip:  swap "binary_search" with a different warmup or exercise
  - tip:  swap "1" with any integer to do several repetitions back-to-back
  
``` Bash
warmup() {
    cd /your/directory/path/here
    if [ $# -eq 0 ]; then
        code test_output.log
        code warmup.py
        python3 main.py
    else
        code test_output.log
        code warmup.py
        python3 main.py "$1" "$2"
    fi
}
```
