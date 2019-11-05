"""SceneSwitch I"""
def switching():
    """ Run Loop """
    current_state = 0       # Start as Off
    next_state = 1
    count = 0       # Counts the Warmwhite state
    while 1:        # Infinite Loop
        data = input()
        if data != "End":
            ### State 0 - Off ###
            if current_state == 0 and next_state == 1:
                current_state = 1                       # On as Daylight
                next_state = 0
 
            elif current_state == 0 and next_state == 2:
                current_state = 2                       # On as Warmwhite
                next_state = 0
                count += 1
 
            ### State 1 - Daylight
            elif current_state == 1 and float(data) <= 6:   # Turn off <= 6 sec
                current_state = 0
                next_state = 2
 
            elif current_state == 1 and float(data) > 6:    # Turn off > 6 sec
                current_state = 0
                next_state = 1
 
            ### State 2 - Warmwhite
            elif current_state == 2:
                current_state = 0
                next_state = 1
 
        else:       # Ends the loop
            break
 
    print(count)

switching()
