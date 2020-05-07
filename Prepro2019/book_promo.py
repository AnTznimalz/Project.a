"""Book Promotion"""
def main():
    """Main Func."""
    book = int(input())
    price = float(input())
    if book > 4 and price > 600:
        price *= 0.9
        print("Promotion: Yes")
        print("Price: %.2f baht" %price)
    else:
        print("Promotion: No")
        print("Price: %.2f baht" %price)
main()
