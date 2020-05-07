"""00xx: Where is your partner!!?"""
def main():
    """Main Func."""
    print("Where is your partner !?")
    msg = input()
    if msg == "On.. on the fridge!" or msg == "In your bag!":
        print("Finally!")
    else:
        print("Last chance. Where is your partner!?")
        msg = input()
        if msg == "On.. on the fridge!" or msg == "In your bag!":
            print("That's it!")
        else:
            print("\\*Toss to the trash*\\")
main()
        