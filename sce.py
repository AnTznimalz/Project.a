"""SceneSwitch I"""
def switch():
    """Switch Function"""
    status = "Off"
    warm = 0
    start = input()
    data1 = 0
    if start == "End":
        status = start
    else:
        status = "On"
        data1 = float(start)
    while status != "End":
        time = input()
        if time == "End":
            status = "End"
        else:
            data2 = float(time)
            if status == "Off":
                status = "On"
            elif status == "On":
                status = "Check"
            elif status == "Check":
                if data2 - data1 <= 6:
                    status = "Warmlight"
                    warm += 1
                else:
                    status = "On"
            elif status == "Warmlight":
                status = "Off"
        data1 = data2
    print(warm)
switch()

