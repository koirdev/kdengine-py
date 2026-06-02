import os, sys, platform
from config import DEBUG_MODE, GAME_VERSION, ENGINE_VERSION
# Writing OS/Hardware information into variables
OS_NAME = os.name # OS Name
PLATFORM_SYS = platform.system() # Platform system
PLATFORM_RELEASE = platform.release() # Platform release
PLATFORM_VERSION = platform.version() # Platform version
PLATFORM_ARCH = platform.architecture() # Platform architecture

if DEBUG_MODE == 1:
	print("Debug mode enabled.")

print(f"Game version: {GAME_VERSION}\nEngine version: {ENGINE_VERSION}\nOS Info:\nPlatform system: {PLATFORM_SYS}\nPlatform release: {PLATFORM_RELEASE}\nPlatform version: {PLATFORM_VERSION}\nPlatform architecture: {PLATFORM_ARCH}")