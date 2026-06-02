import pygame
from config import *
from splashes import random_splash

pygame.display.init()
pygame.font.init()


# Load images
character_img = pygame.image.load('assets/images/player.png')
shirLogo = pygame.image.load('assets/images/shirLogo.png')
bg = pygame.image.load('assets/images/bg.png')
credits = pygame.image.load('assets/images/credits_sign.png')
grass_img = pygame.image.load('assets/images/grass.png')
door1 = pygame.image.load('assets/images/skull_door.png')
loading_screen = pygame.image.load('assets/images/loading_screen.png')

# Resizing images
shirLogo = pygame.transform.scale(shirLogo, (430, 170))
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
credits_sign_img = pygame.transform.scale(credits, (650, 500))
character_img = pygame.transform.scale(character_img,(100,200))
grass_img = pygame.transform.scale(grass_img, (1400,220))
door1 = pygame.transform.scale(door1, (190, 400))
loading_screen = pygame.transform.scale(loading_screen, (WIDTH, HEIGHT))

# Fonts
font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 27)
pause_tips_font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 25)
pause_font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 55)
if SPLASHES == 1:
    splash_text = pygame.font.Font('assets/fonts/Nepoboy-MVMaB.otf', 25)
credits_font = pygame.font.Font('assets/fonts/MotleyForcesRegular-w1rZ3.ttf', 30)
menu_font = pygame.font.Font('assets/fonts/Unbounded-SemiBold.ttf', 50)
level_select_title_font = pygame.font.Font('assets/fonts/Unbounded-SemiBold.ttf', 55)

# Text
if SPLASHES == 1:
    splash_text = splash_text.render(random_splash,False,(245, 224, 86))

build_info_text = font.render(f"{GAME_VERSION}, {ENGINE_VERSION}", False,(252, 250, 250))

level_select_title_text = level_select_title_font.render("Level Select",False,(252,250,250))
if WARNING_TEXT == 1:
    warning_text = font.render("This build is unstable!",False,(252, 250, 250))
help_text = font.render("Released under MIT License.",False,(252, 250, 250))

# Window mode debug text
if DEBUG_MODE == 1:
    if WINDOW_MODE == 2: #Fullscreen mode text
        fullscreen_text = font.render("FULLSCREEN_WINDOW", False,(252,250,250))
    if WINDOW_MODE == 1: # Resizable window text
        resizable_text = font.render("RESIZABLE_WINDOW", False,(252,250,250))
    if WINDOW_MODE == 3: # Hardware window text
        hardware_render_text = font.render("HARDWARE_RENDER_WINDOW", False,(252,250,250)) 
    if WINDOW_MODE == 0: # Default window text
        default_window_text = font.render("REGULAR_WINDOW_MODE", False,(252,250,250))

# Debug mode is enabled text
if DEBUG_MODE == 1:
  build_info_text = font.render(f"DEBUG_MODE - {GAME_VERSION}, {ENGINE_VERSION}",False,(252,250,250))
