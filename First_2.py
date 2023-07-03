
list_1 = list()

for i in range(0,10):
    list_1.append(int(input("Enter your int --> ")))

print("1) Marks;\t2) Exam retake;\t3) Is Scholarship?;")
while True:
    choose = input("Enter choose: ")
    if choose == '1':
        print(list_1)
    elif choose == '2':
        index = int(input("Enter index: "))
        mark = int(input("Enter mark: "))
        list_1.pop(index)
        list_1.insert(index, mark)
    elif choose == '3':
        if sum(list_1) / len(list_1) >= 10.7:
            print("Yes")
        else:
            print("No")
    else:
        break
    
