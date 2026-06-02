import pygame
from config import *
print(WINDOW_MODE)

def toggle_fullscreen():

	if WINDOW_MODE == 0:
		WINDOW_MODE = 2
		window = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

		print(WINDOW_MODE)
	elif WINDOW_MODE == 2:
		WINDOW_MODE == 0
		window = pygame.display.set_mode((WIDTH, HEIGHT))
	

def checkWindow():
	global WINDOW_MODE
	# Regular window.
	if WINDOW_MODE == 0:
	    window = pygame.display.set_mode((WIDTH, HEIGHT))

	# Resizable window.GAME_VERSION, ENGINE_VERSION
	elif WINDOW_MODE == 1:
	    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)     

	# Fullscreen mode.
	elif WINDOW_MODE == 2:
	    window = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)

	# Hardware render.
	elif WINDOW_MODE == 3:
	    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN + pygame.HWSURFACE + pygame.SCALED)

