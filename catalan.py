"""Catalan"""
def cata(num):
    """Func. cata for running catalan"""
    if num == 1:
        return 1
    else:
        return (4*num-2)*cata(num-1)//(num+1)
print(cata(int(input())))
