"""Password Checking"""
def main():
    """Main Func."""
    print("Enter your password...")
    goal = input()
    password = input()
    if password == goal:
        print("Wellcome, Mr.Natchanon.")
    else:
        print("Incorrect, Please Enter password again.")
        password = input()
        if password == goal:
            print("Wellcome, Mr.Natchanon.")
        else:
            print("Incorrect, Please Enter password again.")
            password = input()
            if password == goal:
                print("Wellcome, Mr.Natchanon.")
            else:
                print("Incorrect, Please Enter password again.")
                password = input()
                if password == goal:
                    print("Wellcome, Mr.Natchanon.")
                else:
                    print("Incorrect, Try again in 30 seconds.")
main()
