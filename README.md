# Algorithm training
Daily warmups for SWE interview prep sessions  
Inspired by my classical music training


## To Use
1. Open your terminal
2. Run one of the following terminal commands
3. Open "warmup.py" in your IDE
4. Code your solution
5. Hit "Enter" in your original terminal window and repeat from step 3



## Terminal commands
Random  
`python3 main.py`

Pick one from below  
`python3 main.py binary_search`

Pick one for multiple repetitions  
`python3 main.py binary_search 5`



## Contents
- binary_search
- oop_basics
- sliding_window
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
2. Then type `warmup` in your terminal to do a problem in VS Code  
  
``` Bash
warmup() {
    cd /your/directory/path/here
    if [ $# -eq 0 ]; then
        code warmup.py
        python3 main.py
    else
        code warmup.py
        python3 main.py "$1" "$2"
    fi
}
```