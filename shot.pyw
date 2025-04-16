import pygame
import keyboard


pygame.init()


pygame.joystick.init()



joysticks = []


equals_pressed = False


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joy.init()
            joysticks.append(joy)
            print(f"Joystick bağlandı: {joy.get_name()}")

        if event.type == pygame.QUIT:
            run = False

    for joystick in joysticks:
        
        vert_move = joystick.get_axis(1)

        if abs(vert_move) > 0.90:
            if not equals_pressed:  
                keyboard.press('z')  
                equals_pressed = True
                print("basıldı") 
        else:
            if equals_pressed:  
                keyboard.release('z')  
                equals_pressed = False  
                print("bırakıldı")

    
    pygame.time.delay(10)

t
pygame.quit()
