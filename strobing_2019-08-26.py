# [ ] synchronize while loop to display refresh

# need: pip install pywin32
# need: pip install pyqt5

import pygame
import win32api
import win32con
import win32gui

pygame.init()
# pygame.mixer.quit()
screen_width = 720
screen_height = 540

screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
# dark_red = (139, 0, 0)
game_frames = 0

# Set window transparency color to hide window border
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


clock = pygame.time.Clock() # Create a clock object
FPS = 144 # set to your screen refresh rate

#? possible optimization to stuttering?
#myimage = pygame.image.load("black square.png")
#myimage = pygame.transform.scale(myimage, (screen_width, screen_height))
#imagerect = myimage.get_rect()

#screen.set_alpha(256/2) # the higher the alpha the more blur reduction
game_frames = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if game_frames < 6: #2 minimum, cuts frames displayed in half, 6 from 144hz for 24fps
        #screen.blit(myimage, imagerect)
        #self.image.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)

        screen.fill((0,0,0))  # black
        game_frames += 1
    else:
        #screen.blit(myimage, imagerect)

        screen.fill(fuchsia)
        game_frames = 1

    #pygame.display.flip() #update the entire surface
    pygame.display.update() #update part of the surface

    clock.tick(FPS)