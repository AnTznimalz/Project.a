"""Turnstile"""
def count():
    """Func. Count for counting how many people pass the turnstile"""
    people = 0
    status = "Lock"
    while True:
        message = input()
        if message == "C":
            status = "Unlock"
        elif message == "P" and status == "Unlock":
            people += 1
            status = "Lock"
        elif message == "END":
            break
    print(people)
count()
