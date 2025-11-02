import functions
import os
os.makedirs("PMS", exist_ok=True)
logged_in_user = None

while True:
    choice = functions.main_menu()
    if choice == "1": 
        if logged_in_user:
            functions.quit_session(logged_in_user)
            logged_in_user = None

        username = functions.user_login()
        if username:
            logged_in_user = username
            while True:
                print("\n--- User Panel ---")
                print("1. Logout to Main Menu")
                user_choice = input("Please choose an option: ")

                if user_choice == "1":
                    functions.quit_session()
                else:
                    print("Invalid option. Please try again.")

    elif choice == "2": 
        if logged_in_user:
            functions.quit_session(logged_in_user)
            logged_in_user = None

        admin_name = functions.admin_login()
        if admin_name:
            logged_in_user = admin_name
            while True:
                print("\n--- Admin Panel ---")
                print("1. Logout to Main Menu")
                admin_choice = input("Please choose an option: ")

                if admin_choice == "1":
                    functions.quit_session(logged_in_user)
                    logged_in_user = None
                    break
                else:
                    print("Invalid option. Please try again.")

    elif choice == "3": # Quit Program
        if logged_in_user:
            functions.quit_session(logged_in_user)
        print("Quitting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")