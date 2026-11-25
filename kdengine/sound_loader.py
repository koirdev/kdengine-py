import pygame
from config import  MUSIC, SFX
from os_info import PLATFORM_SYS

def loadAudio(): # .py file name

    pygame.mixer.init()

    if PLATFORM_SYS == 'Linux':
        diff_path = ""
    else:
        if PLATFORM_SYS == 'Windows':
            diff_path = ""            
        else:
            print(f"Warning: A different path for sound that are not identified.")
    print(f"different path for sound is: {diff_path} - for {PLATFORM_SYS}.")

    # Load music.
    if SFX == 1:
    # Load sound effects.
        global clickSound, click2Sound, whooshSound
        clickSound = pygame.mixer.Sound(diff_path + 'assets/sfx/click.wav')
        click2Sound = pygame.mixer.Sound(diff_path + 'assets/sfx/click2.wav')
        whooshSound = pygame.mixer.Sound(diff_path + 'assets/sfx/whoosh.wav')

loadAudio()

