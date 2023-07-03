##List
# fruit = ['apple', 'plum', 'banana','orange']
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

# import random
# numbers = [random.randint(20,50) for i in range(10)]
# print(numbers)

# letters = [s for s in "banana"]
# print(''.join(letters))

# line = 'reverv erverwjwqed wqibdqiw wqibd iwq wqibd'

# words = line.split(' ')
# print(words)

# colors = ['red', 'blur', True, 555]
# colors.append('green')
# colors.insert(2, 'pink')
# colors.extend(['brown', 'violet', 'white'])
# colors.remove('red')

# import random
# numbers = [random.randint(10,100) for i in range(10)]

# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))

# numbers.sort(reverse=True)
# print("Print list :: ", numbers)

# colors = ['red', 'green', 'yellow', 'blue', 'orange']
# cloneColors = colors
# print(colors is cloneColors)
# print(colors)
# print(cloneColors)


# #cloneColors = colors.copy()
# cloneColors = list(colors)

# colors[0] = 'line'
# print(colors)
# print(cloneColors)

# classwork

j = int(input("Enter len --> "))
number_for_search = int(input("Enter number for search --> "))
list_1 = list()
count = 0
for i in range(0,j):
    list_1.append(int(input("Enter your int --> ")))
    if list_1[i] == number_for_search:
        count += 1
print("count = ",count)