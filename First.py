j = int(input("Enter len --> "))
number_for_search = int(input("Enter number for search --> "))
list_1 = list()
count = 0
for i in range(0,j):
    list_1.append(int(input("Enter your int --> ")))
    if list_1[i] == number_for_search:
        count += 1
print("count = ",count)