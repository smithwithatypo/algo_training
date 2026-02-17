import sys
import commands.run_warmup
import commands.run_problem

from data.warmups import WARMUPS
from data.problems import PROBLEMS


def print_available(category: str):
    if category == "warmup":
        print("Available warmups:")
        for key in WARMUPS.keys():
            print(f"  - {key}")
    elif category == "problem":
        print("Available problems:")
        for key in PROBLEMS.keys():
            print(f"  - {key}")
    else:
        print("Error: need warmup or problem for category")


def select_int(arr):
    for item in arr:
        if item.isdigit():
            return int(item)
    else:
        return None


if __name__ == "__main__":
    args = set(sys.argv[1:])
    int_arg = select_int(args)

    if "-w" in args:
        if "all" in args:
            for problem_name in WARMUPS:
                commands.run_warmup.warmup(problem_name, 3)
        elif "-h" in args:
            print_available("warmup")
        elif args & set(WARMUPS.keys()):
            warmup_name = (args & set(WARMUPS.keys())).pop()
            if int_arg:
                commands.run_warmup.warmup(warmup_name, int_arg)
            else:
                commands.run_warmup.warmup(warmup_name)
        elif int_arg:
            commands.run_warmup.warmup("", int_arg)
        else:
            commands.run_warmup.warmup()
    elif "-p" in args:
        if "all" in args:
            for problem_name in PROBLEMS:
                commands.run_problem.problem(problem_name, 3)
        elif "-h" in args:
            print_available("problem")
        elif args & set(PROBLEMS.keys()):
            problem_name = (args & set(PROBLEMS.keys())).pop()
            if int_arg:
                commands.run_problem.problem(problem_name, int_arg)
            else:
                commands.run_problem.problem(problem_name)
        elif int_arg:
            commands.run_problem.problem("", int_arg)
        else:
            commands.run_problem.problem()
    else:
        print("Error: need -w or -p flag to run")
