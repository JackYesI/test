list_1 = list()

for i in range(0,12):
    list_1.append(int(input("Enter your int --> ")))

max = max(list_1)
min = min(list_1)

for i in range(0, 12):
    if list_1[i] == max:
        print("max = 0{}".format(i+1))
    if list_1[i] == min:
        print("min = 0{}".format(i+1)) 