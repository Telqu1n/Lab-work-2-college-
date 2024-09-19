import random
def number_guessing():
    compnum = random.randint(1,100)

    num1 =  int(input("Enter a number:"))
    flag = True 
    while flag:
        if num1 < compnum:
            print("The number your entered is lower than the number")
            num1 =  int(input("Enter a number:"))
            count =+ 1

        elif num1 > compnum:
            print("The number your entered is higher than the number")
            num1 =  int(input("Enter a number:"))
        elif num1 == compnum:
            print("The number your entered is equal to the number")
            break
        else:
            print("Invalid input")
            continue
    print("The number is:", compnum)
number_guessing()