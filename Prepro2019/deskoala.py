"""But it's was me. Des Koala!"""
def main():
    """Main Func."""
    point = float(input())
    card = int(input())
    point -= card * 400
    print("LP: %.4f" %max(point, 0))
main()
