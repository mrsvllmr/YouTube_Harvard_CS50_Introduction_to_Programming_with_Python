import random
import statistics

# random list as a basis
list = []
for _ in range(0, 20):
    list.append(random.randint(0, 10))
print("List: ", list)

# mean
print("Mean: ", statistics.mean(list))
