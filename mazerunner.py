def turn_right():
    turn_left()
    turn_left()
    turn_left()   
def turn_loop():   
    turn_right()
    move()
    turn_right()
    move()
while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear()==True:
        move()
    elif right_is_clear()!=True:
        turn_left()
        
            
            
  
