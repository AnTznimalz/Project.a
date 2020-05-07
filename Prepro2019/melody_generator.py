"""Melody Generator"""
def main():
    """Main Func."""
    print("C D E F G")
    draw(input())
    draw(input())
    draw(input())
    draw(input())
    draw(input())
def draw(wow):
    """Draw Func."""
    note = ord(wow) - 67
    print(" " * note * 2 + "O")
main()
