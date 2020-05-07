"""Volume"""
import math
def main():
    """"Func. Main"""
    radius_1 = float(input())/2
    radius_2 = float(input())/2
    vol_1 = vol(radius_1)
    vol_2 = vol(radius_2)
    ans = abs(vol_1-vol_2)
    print("%.3f" %ans)
def vol(radius):
    """Func. vol for finding volume of ball"""
    volume = (4/3) * math.pi * (radius**3)
    return volume
main()
