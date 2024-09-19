def num_check():


    while True:
        num = int(input("Enter a number:"))
        if num <10:
            print ("Too low")
        elif num >20:
            print ("Too high")
        else:
            print("Thank you")
            break
    
num_check()