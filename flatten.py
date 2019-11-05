"""
Flatten by ศิษย์เทพปอง#2
special thank to Aj.Cho
"""
import json
def flat(box):
    """Func. flat for making flat list"""
    bag = []
    for i in box:
        if isinstance(i, list):
            box.extend(i)
        else:
            bag.append(i)
    bag.sort(reverse=True)
    return bag
print(flat(json.loads(input())))
