
# Algorithm training  

Daily warmups for SWE interview prep sessions  
Inspired by classical music training

## How To Use

1. Open your terminal
1. Install the dependencies  
    - `pip install -r requirements.txt`
1. Run any of the Terminal Commands from the next section
1. Open `userInput/warmup.py` or `userInput/problem.py`
1. Input your solution
1. Hit the `Enter` key in your original terminal window and repeat from step 3

## Terminal Commands

- Random warmup  
`python3 main.py -w` 

- See all available warmups  
`python3 main.py -w -h`

- Do a warmup for 1 repetition 
`python3 main.py -w binary_search`

- Do a warmup for 3 repetitions (use any positive integer)
`python3 main.py -w binary_search 3`

- To do a problem (harder than warmups), just swap `-p` instead of `-w`  
`python3 main.py -p dp 5`

## (optional) Quickstart automation for MacOS or Linux

1. Copy/paste the functions below into your .zshrc file and restart your terminal  
2. Then type `warmup` (or `problem`) in your terminal to do a problem in VS Code  
  - or `warmup binary_search` to do once
  - or `warmup 5` to do 5 reps of a random warmup
  - or `warmup binary_search 5` to do 5 reps of binary_search
  - or `warmup all` to do 3 reps of all available warmups
  
``` Bash
warmup() {
    cd /Users/dude/projects/python/algo-training
    if [ $# -eq 0 ]; then
        code userInput/warmup.py userInput/test_output.log
        python3 main.py -w
    elif [ $# -eq 1 ]; then
        code userInput/warmup.py userInput/test_output.log
        python3 main.py -w "$1"
    else
        code userInput/warmup.py userInput/test_output.log
        python3 main.py -w "$1" "$2"
    fi
}
problem() {
    cd /Users/dude/projects/python/algo-training
    if [ $# -eq 0 ]; then
        code userInput/problem.py userInput/test_output.log
        python3 main.py -p
    elif [ $# -eq 1 ]; then
        code userInput/problem.py userInput/test_output.log
        python3 main.py -p "$1"
    else
        code userInput/problem.py userInput/test_output.log
        python3 main.py -p "$1" "$2"
    fi
}
```
