j = int(input("Enter len --> "))

list_1 = list()

for i in range(0,j):
    list_1.append(int(input("Enter your int --> ")))

print("sum = {}, arg = {}".format(sum(list_1), sum(list_1)/len(list_1)))