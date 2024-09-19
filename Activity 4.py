def adding_names_to_party():


    list = [] 
    name = input("Enter a name of someoen you want to invite to a party ")
    list.append (name)
    
    print (list)

    flag = true 
    while flag:
        user_input = input("Do you want to invite someone eles to the party?").upper()
        
        if user_input == "YES" or user_input == "Y":
            name = input("Enter a name of someoen you want to invite to a party ")
            list.append (name)
        elif user_input == "NO" or user_input == "N":
            break 
        else:
            print("Invalid input")
            continue