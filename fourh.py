n = int(input("Enter N --> "))

list_1 = list()

for i in range(0,n):
    list_1.append(int(input("Enter your int --> ")))

sum_min = 0
min = min(list_1)
max = max(list_1)
mul = 1

for i in range(0,n):
    if i < 0:
        sum_min