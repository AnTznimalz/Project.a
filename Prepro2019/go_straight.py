"""Go straight Go straight Go straight!!!!"""
def main():
    """Main Func."""
    stack = 0
    done = 0
    time = 0
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    stack, done, time = wow(input(), stack, done, time)
    if not done:
        if time != 0:
            print("%d minute." %time)
        else:
            print("Good job Mean!!!")
def wow(order, stack, done, time):
    """Wow Func."""
    if order == "Go straight":
        stack += 1
        time += 10
    else:
        stack = 0
    if stack == 3:
        print("Welcome to Chaimai!!!")
        done = 1
    return stack, done, time
main()
