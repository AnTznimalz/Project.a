"""Water bill"""
def main():
    """Main Func."""
    water = int(input())
    money = 100
    if water <= 5:
        print("%.2f baht" %money)
    else:
        money += (water-5) * 18.5
        print("%.2f baht" %money)
main()
