#KD_ENGINE_CONFIG:

#:WINDOW_RESOLUTION:
WIDTH = 1280		#1500 - for test
HEIGHT = 720		#1080 - for test

#:SETTINGS:
FPS = 60
WINDOW_MODE = 0 # 0 - regular, 1 - resizable, 2 - fullscreen, 3 - hardware render.
WARNING_MESSAGE = 0 # old depending shit.
MUSIC = 1 # 0 - disabled, 1 - enabled.
SFX = 1  # 0 - disabled, 1 - enabled.
WARNING_TEXT = 1 # Shows text "This build is unstable!" on 'Main Menu' screen. 0 - disabled, 1 - enabled. 
SPLASHES = 1 # Random text on the 'Main Menu' screen. (splashes.py). 0 - disabled, 1 - enabled. 
ENGINE_VERSION = "KD Engine ver. 0.1"
GAME_VERSION = "ForkMania ver 0.1" # Game version (Shows on the console and on the 'Main Menu' screen).
CONTROLS = 1 # 1 - Keyboard, 2 - XBOX 360 Controller(s). To change the button assignments, go to the "controls" path. For the keyboard, use "keyboard_config.py". For the XBOX 360 controller(s), use "xbox360_config.py".
GAMEPAD_VIBRATION = 0 # in dev.
ENABLE_DISCORD = 1 # Discord support. (Discord Rich Presence). 0 - disabled, - 1 - enabled.

#:PATHS_TO_RESOURCES:
url = "http://storage.kdvv.su/game_assets/dev/forkmania/zip/assets.zip" # URL to download assets.
ASSETS_DIR = "assets" # 'assets' directory.
SCREENSHOTS_DIR = "screenshots" # 'screenshots' directory. 
SCREENSHOTS_FILE_PATH = SCREENSHOTS_DIR + "/screenshot.jpg" # 'screenshot.jpg' file path/name. (screenshots/screenshot.jpg).
LOG_FILE_NAME = "KD_Engine.log" # Log file name.

#:TOOLS:
DEBUG_MODE = 1 # 0 - disabled, 1 - enabled.
LEVEL_SELECT = 0 # If 'LEVEL_SELECT' variable equals '1', then, on the start of the game, will be used the 'Level Select' menu screen, instead of 'Main Menu' screen.
LOGGING = 0 # Logging all game stuff. (Log file path/name - KD_Engine.log). 0 - disabled, 1 - enabled.

#:SERVER_CLIENT_SETTINGS:
game_client_id = 'shirClient' # Game ID. (in dev).
IP = 'localhost'
PORT = 2555
# To run a test local server, follow the path "localhost_server" and run the file "server.py" or compile the EXE file using the PyInstaller library. 


