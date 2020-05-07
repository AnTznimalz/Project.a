"""Login Successful!!"""
def main():
    """Main Func."""
    name = input()
    sur = input()
    sex = input()
    use = input()
    psw = input()
    u_con = input()
    p_con = input()
    print(use)
    print("*"*len(psw))
    if use == u_con and psw == p_con:
        print("Login Successful !!")
        if sex == "Male":
            print("Welcome Back !! Mr. %s %s" %(name, sur))
        else:
            print("Welcome Back !! Mrs. %s %s" %(name, sur))
    else:
        print("Login Failed !!")
main()
