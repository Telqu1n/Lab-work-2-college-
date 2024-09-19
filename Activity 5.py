compnum = 50

num1 =  int(input("Enter a number:"))
flag = True 
while flag:
    if num1 < compnum:
        print("The number your entered is lower than the number")
        num1 =  int(input("Enter a number:"))
    elif num1 > compnum:
        print("The number your entered is higher than the number")
        num1 =  int(input("Enter a number:"))
    elif num1 == compnum:
        print("The number your entered is equal to the number")
        break
    else:
        print("Invalid input")
        continue