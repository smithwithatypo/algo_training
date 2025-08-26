import os
import subprocess
import random
from problems import PROBLEMS

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def write_problem(problem_name, rep_num=None, total_reps=None, warning=""):
    problem = PROBLEMS[problem_name]
    
    header = f"# Rep {rep_num}/{total_reps} - {problem['title']}\n" if rep_num else f"{problem['title']}\n"
    if warning:
        header += f"{warning}\n"
    header += "\n\n"
    
    content = header + problem['template']
    
    with open('warmup.py', 'w') as f:
        f.write(content)

def run_tests():
    result = subprocess.run(['python3', '-m', 'pytest', 'warmup.py', '-v', '--tb=short', '--maxfail=10'], 
                          capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def warmup(problem_name=None, reps=1):
    if not problem_name:
        problem_name = random.choice(list(PROBLEMS.keys()))
    
    warning = ""
    for rep in range(1, reps + 1):
        
        while True:
            clear_screen()
            write_problem(problem_name, rep, reps, warning)
            
            input("Press Enter when ready to test...")
            
            passed, output = run_tests()
            with open('test_output.log', 'w') as f:
                f.write(f"passed: {passed}\n\n")
                f.write(f"pytest output:\n {output}\n\n")
                f.write("#" * 50 + "\n")
                f.write("your code:\n")
                f.write("#" * 50 + "\n")
                try:
                    with open('warmup.py', 'r') as warmup_file:
                        f.write(warmup_file.read())
                except FileNotFoundError:
                    f.write("warmup.py file not found")            
            
            if passed:
                warning = ""
                if rep == reps:
                    clear_screen()
                    print("🎉 All reps complete!")
                break
            else:
                warning = f"# ⚠ Failed test(s) last time"
                break
    if warning == "":
        print("passed all tests!")
    else:
        print("last attempt failed test(s)")



if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    
    if len(args) == 0:
        warmup()
    elif len(args) == 1:
        warmup(args[0])
    else:
        warmup(args[0], int(args[1]))