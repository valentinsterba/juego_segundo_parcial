from vars_const import HEIGHT
cowboy_x = 50
cowboy_y = HEIGHT - 100
cowboy_width = 50
cowboy_height = 50
cowboy_jump = False
jump_speed = 15
gravity = 1 
cowboy_pace = 0 
def cowboy ():
    if cowboy_jump:
        cowboy_pace -= gravity
        cowboy_y -= cowboy_pace
        if cowboy_y >= HEIGHT - cowboy_height - 50:
            cowboy_y = HEIGHT - cowboy_height - 50
            cowboy_jump = False
            cowboy_pace = 0 