"""
- Generate a random number in range (1,5), both boundaries included
- All these numbers have certain weights:
    o Example: 5 - 0.4, 4: 0.3, 3: 0.17, 2: 0.09, 1: 0.04
    o Playing with weights will get more optimal results
- Then get a random group/mv/idol in the priority group outputted.
"""

from  random import choices
from random import randint
population = [1,2,3,4,5]
weights = [0.02, 0.08, 0.15, 0.30, 0.45]

million_samples = choices(population, weights, k=10**6)
from collections import Counter
print(Counter(million_samples))

# import json

# sample = choices(population, weights)

# with open('priority.json', 'r') as p:
#     data = json.load(p)
#     groups = data[str(sample[0])]
#     group_idx = randint(0, len(groups) - 1)
#     group = groups[group_idx]
