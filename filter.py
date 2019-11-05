"""Filter by ศิษย์เทพปอง#2"""
import json
def hig(text=input(), target=float(input())):
    """Func. hig for finding the better or equal to the target"""
    check = True
    text = json.loads(text)
    order = sorted(text)
    for i in order:
        score = text.get(i)
        if score >= target:
            check = False
            print(i + '\t%.2f'%score)
    if check == True:
        print("Nope")
hig()
