def enter_number_until_its_over_5():
    user_input = int(input("Enter a number:"))

    while user_input < 5:
        user_input = int(input("Enter a number:"))
        if user_input > 5:
            break
        else:
            continue
    else:
        print("The number entered is 5")
    
enter_number_until_its_over_5()