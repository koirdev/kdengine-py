import pygame
from config import *

pygame.mixer.init()

# Load music.
if MUSIC == 1:
    def MainMenuMusic():
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load('assets/sound/Scattle - To The Top.mp3')
        #pygame.mixer.music.play(-1)
        pass
        
    def LevelSelectMusic():
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load('assets/sound/internetsmenu.mp3')
        #pygame.mixer.music.play(-1)
        pass


# Load sound effects.
if SFX == 1:
    clickSound = pygame.mixer.Sound('assets/sfx/click.wav')
    click2Sound = pygame.mixer.Sound('assets/sfx/click2.wav')
    whooshSound = pygame.mixer.Sound('assets/sfx/whoosh.wav')


