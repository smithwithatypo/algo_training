from data.warmups import WARMUPS
from data.problems import PROBLEMS

warmup_keys = list()
problem_keys = list()

for key in WARMUPS.keys():
    warmup_keys.append(key)

for key in PROBLEMS.keys():
    problem_keys.append(key)


print(f"warmups available: {warmup_keys}")
print("\n")
print(f"exercises available: {problem_keys}")
