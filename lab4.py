while True:  
    user_input = input("Enter a number: ")

    try:
        user_number = int(user_input)
        if user_number > 0:
            print(f"{user_number} is a positive number.")
        elif user_number < 0:
            print(f"{user_number} is a negative number.")
        else:
            print("You entered zero.")
        
        break

    except ValueError:
        print("That's not a valid number. Please enter an integer.")
