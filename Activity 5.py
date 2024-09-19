def number_counting_game():


    compnum = 50
    count = 0

    num1 = int(input("Enter a number:"))
    flag = True
    while flag:
        count += 1  # Increment count for each input
        if num1 < compnum:
            print("The number you entered is lower than the number")
            num1 = int(input("Enter a number:"))
        elif num1 > compnum:
            print("The number you entered is higher than the number")
            num1 = int(input("Enter a number:"))
        elif num1 == compnum:
            print("The number you entered is equal to the number")
            break
        else:
            print("Invalid input")
            continue

    print("The number is:", compnum, "You guessed", count, "times")
    
number_counting_game9()
