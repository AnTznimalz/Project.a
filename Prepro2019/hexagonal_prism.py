"""Hexagonal Prism"""
def main():
    """Main Func."""
    length = float(input())/100
    high = float(input())/100
    hex_area = 6*(((3**0.5)/4) * (length**2))
    rec_area = high * length
    all_area = (hex_area * 2) + (rec_area * 6)
    print("%.2f squaremetre" %all_area)
main()
