total = 0 

num1 =  int(input("Enter a number:"))
num2 =  int(input("Enter a number:"))

total = num1 + num2
    
flag = True 
while flag: 
    user_input = input("Enter a do you want to add another numer?:").upper()
    
    if user_input == "YES"or user_input == "Y":
        choice = int(input("Enter a number:"))
        total += choice
    elif user_input == "NO" or user_input == "N":
        print("The total is:", total)
        break
    else :
        print ("Invalid input")
        continue
