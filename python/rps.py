def execute_option(option):
    if option == '1':
        print("You chose Option 1")
        # Add your code for Option 1 here
    elif option == '2':
        print("You chose Option 2")
        # Add your code for Option 2 here
    elif option == '3':
        print("You chose Option 3")
        # Add your code for Option 3 here
    else:
        print("Invalid option")

while True:
    print("\nChoose one of the following options:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

    user_choice = input("\nEnter your choice: ")
    if user_choice == '4':
        break

    execute_option(user_choice)