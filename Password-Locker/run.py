import random
from user import User

def main():


while True: 
    print("welcome to password locker !!!")
    print('\n')
    print("Select a short code to navigate through to create new user use 'nu':To login to your account 'lg' or 'ex' to exit")
    short_code = input().lower()
    print('\n')

    if short_code =='nu':
        print('create username')
        created_user_name = input()

        print('create password'
        created_user_password = input()

        print('confirm password')
        confirm_password = input()


        while confirm_password != created_user_password
            print("invalid password didn't match!!")
            print("enter your your password")
            created_user_password = input()
            print("confirm your password")
            confirm_password = input()
        else:
            print(f"congragulations (created_user_name): account creation successful!!")
            print('\n')
            print("proceed to login")
            print("Usename")
            entered_username= input()
            print ("your password")
            entered_password = input()

        while entered_username != created_user_name or entered_password != created_user_password
            print("invalid password or username")
            print("Username")
            entered_username = input()
            print("password")
            entered_password = input()

        else:
            print(f"welcome : (entered_username) to your account")
            print('\n')

    elif short_code =='lg':
        print("welcome")
        print("Enter user name")
        default_user_name = input()


        print("Enter password")
        default_user_password = input()
        print('\n')
        while default_user_name != 'testuser' or default_user_password != '09876'
            print("Wrong userName or password.Username 'tsetuser' and password '09876'")
            print("Enter user name")
            default_user_name = input()

        print("Enter password")
        default_user_password = input()
        print('\n')
        else:
            print("login success")
            print('\n')
            print('\n')

    elif short_code =='ex'
        break
    else:
                print("Enter valid code to continue")


if __name__ == '__main__':
    unittest.main()


        