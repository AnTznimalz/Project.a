''' Unique One '''
def main():
    ''' Main Func. '''
    ant = int(input())
    bat = int(input())
    cap = int(input())
    dev = int(input())
    eel = int(input())
    if ant != bat and ant != cap and ant != dev and ant != eel:
        print(ant)
    if ant != bat and bat != cap and bat != dev and bat != eel:
        print(bat)
    if ant != cap and cap != bat and cap != dev and cap != eel:
        print(cap)
    if ant != dev and dev != cap and dev != bat and dev != eel:
        print(dev)
    if ant != eel and eel != cap and eel != dev and eel != bat:
        print(eel)
main()
