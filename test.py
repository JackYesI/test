##List
fruit = ['apple', 'plum', 'banana','orange']
# rnumbers = list((2,4,5,76,8,3,2))

# # print(fruit)
# # print(rnumbers)
# # print(fruit[-1])

# # for i in fruit[0::2]:
# #     print(i)

# for item in fruit[0::2]:
#     for s in item:
#         print(s,end="_")
#     print()


# print('banana' in fruit)

import random
numbers = [random.randint(20,50) for i in range(10)]
print(numbers)

letters = [s for s in "banana"]
print(''.join(letters))

line = 'reverv erverwjwqed wqibdqiw wqibd iwq wqibd'

words = line.split(' ')
print(words)