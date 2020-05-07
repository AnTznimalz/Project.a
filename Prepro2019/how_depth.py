"""How depth is it"""
import math
def main():
    """Main Func."""
    node = int(input())
    floor = math.log(node, 2) + 1
    print(int(floor))
main()
