# How to contribute to this project

## How to contribute
1. Fork the repo
1. Make a new branch on your local git  
    - `$ git switch -c my-new-branch`
1. Make a new pull request  
    1. code your changes
    1. commit locally
    1. push to your github repo (probably named "origin")
    1. open a pull request
    1. reach out to me if I'm missing any steps!

## LLM prompt
- NOTE: replace {new_algorithm} on line 3 with your new algorithm

``` 
Be a senior software engineer at a big tech company who interviews engineers.

We're building a tool in python that lets engineers study algorithms repetitively. We're adding a new problem today. 

Can you write a new problem with some simple test cases for {new_algorithm} in this format? 

    "binary_search": {
        "title": "Binary Search",
        "template": '''def binary_search(arr, target):
    """
    Find target in sorted array. Return index or -1 if not found.
    arr = [1,3,5,7,9], target = 5 -> return 2
    """
    # your code here
    pass

def test_binary_search():
    assert binary_search([1,3,5,7,9], 5) == 2
    assert binary_search([1,3,5,7,9], 1) == 0
    assert binary_search([1,3,5,7,9], 9) == 4
    assert binary_search([1,3,5,7,9], 4) == -1
    assert binary_search([], 1) == -1
''',

```
