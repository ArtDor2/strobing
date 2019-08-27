# [ ] synchronize while loop to display refresh

# need: pip install pywin32
# need: pip install pyqt5

import pygame
import win32api
import win32con
import win32gui

pygame.init()
# pygame.mixer.quit()
screen = pygame.display.set_mode((720, 540), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
# dark_red = (139, 0, 0)
game_frames = 0

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

obj_transparancy = 1
FPS = 120
clock = pygame.time.Clock() # Create a clock object

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if obj_transparancy == 1:
        # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 100, 600, 600))
        screen.fill(fuchsia)
    else:
        screen.fill((0,0,0))  # Transparent background
    
    pygame.display.flip()
    # pygame.display.update()
    clock.tick(FPS)

    game_frames += 1
    if game_frames == 4:
        game_frames = 0
        obj_transparancy *= -1
