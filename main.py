print("Loading game...")
import sys, pygame, math, subprocess, os
sys.path.append("kdengine/")
from kdengine import *

pygame.init()

# Checks for initialization error.
game_init = pygame.init()
if(game_init[1]>0):
    MainCoreInitError()
    sys.exit()

if WINDOW_MODE > 3:
    WindowModeError()
    sys.exit()

# ---- Window options ----

# Regular window.
if WINDOW_MODE == 0:
    window = pygame.display.set_mode((WIDTH, HEIGHT))

# Resizable window.GAME_VERSION, ENGINE_VERSION
elif WINDOW_MODE == 1:
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)     

# Fullscreen mode.
elif WINDOW_MODE == 2:
    window = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN + pygame.SCALED)

# Hardware render.
elif WINDOW_MODE == 3:
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN + pygame.HWSURFACE + pygame.SCALED)

def mainLoadingScreen(): # Main loading screen (For example, if the game loads not completly, or not correctly).
    main_loading_font = pygame.font.SysFont("Arial", 36)
    text_surface = font.render(f"Loading...", False, (255, 255, 255)) 
    text_rect = text_surface.get_rect(center=(60, 20))
    window.fill((0, 0, 0))
    window.blit(text_surface, text_rect)
    pygame.display.flip()
mainLoadingScreen()

if ENABLE_DISCORD == 1: # Connects to the Discord client if 'ENABLE_DISCORD' variable is enabled ('1'). 
    pass

if CONTROLS == 2: # XBOX 360 Controls (In the config file it's '2').
    try:
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init() # Initialize connected controllers(s).

        print(f"Initialized gamepad(s): {joystick.get_name()}") # Shows initialized controller(s) on console.

        # Excepts the pygame error (For example if connected controller(s) was not found and the 'CONTROLS' variable is '2').
    except pygame.error:
        print("WARNING: Controller(s) not detected. Change the 'CONTROLS' parameter to '1' to use keyboard controls. Keyboard controls will be automatically switched over.")
        # If connected controller(s) was not found and the 'CONTROLS' variable equals '2', then, it's changes to: '1' - Keyboard input.
        CONTROLS = 1


# Window title and icon
pygame.display.set_caption("ForkMania") # Title.
icon = pygame.image.load('assets/images/icon.png') # Icon.
pygame.display.set_icon(icon)
clock = pygame.time.Clock() 

# Menu Sections
if DEBUG_MODE == 1:
    items = ['Level 1','Multiplayer','Open log file','Level select','Exit game'] # If 'DEBUG_MODE' variable equals '1'.
else:
    items = ['Play','Settings','Exit game'] # Normal mode (If 'DEBUG_MODE' variable equals '0' or more).

# Section colors
CYAN = (255, 255, 255) # If the cursor switchs on section.
DARK_CYAN = (119, 119, 120) # If the cursor NOT switchs on section.

# Character position
character_x = 400
character_y = 300
character_speed = 5


selected_section = 0

# Scene switcher
current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene

def fade_in(width, height): # Fade in - (When qutting to menu or enters on a 'GameScene').
    fade = pygame.Surface((width, height))
    fade.blit(loading_screen,(0,0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        window.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)


def MainMenu():
    if MUSIC == 1:
        MainMenuMusic()
    global running, selected_section, shirLogo_x, CONTROLS
    menuX = 1
    menu_speed = 15
    menu_spacing = 0
    running = True
    if LEVEL_SELECT == 1:
        mainLoadingScreen()
        running = False
        Level_Select() 
    while running:
        # Quit Event
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    if ENABLE_DISCORD == 1:
                        discordClientClose()
                        print("Discord API closed.")
                    running = False
                    pygame.quit()
                    sys.exit()


            # 'F7' - To take a screenshot.
                if e.type == pygame.KEYUP:
                    if e.key == screenshot_keyboard:
                        checkScreenshotsFolder()
                        print("Taking a screenshot...")
                        pygame.image.save(window, SCREENSHOTS_FILE_PATH)
                        print(f"Done. Saved in {SCREENSHOTS_FILE_PATH} directory.")
                        openScreenshotFile()

            # Keyboard input.
                if e.type == pygame.KEYDOWN:
                    if e.key == up_menu_section_keyboard:
                        selected_section -= 1
                        if SFX == 1:
                            clickSound.play()
                    elif e.key == down_menu_section_keyboard:
                        selected_section += 1
                        if SFX == 1:
                            clickSound.play()
                    elif e.key in [enter_keyboard]:
                        if SFX == 1:
                            whooshSound.play()

            # Menu tabs
                        if items[selected_section] == 'Exit game': running = False, pygame.quit(), sys.exit()
                        if items[selected_section] == 'Open log file': OpenLogFile()
                        if items[selected_section] == 'Multiplayer': mainLoadingScreen(), RunClient()
                        if items[selected_section] == 'Level select': running = False, Level_Select()
                        if items[selected_section] == 'Level 1': running = False, Level_1() 
                        if items[selected_section] == 'Play': pass
                        #if items[selected_section] == 'Initialize local host': subprocess.Popen("modules\localhost_server\server.py, 1", shell=True)
                    selected_section = selected_section % len(items)

       # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == quit_from_game_keyboard:
                    if ENABLE_DISCORD == 1:
                        discordClientClose()
                    sys.exit()

        # Render graphics
            #window.blit(bg,(0, -0))
            window.fill((84, 26, 145))
            window.blit(shirLogo,(420,0))
            window.blit(build_info_text, (0,30))
            if WARNING_TEXT == 1:
                window.blit(warning_text, (0,0))
            window.blit(help_text, (0,60))
            if DEBUG_MODE == 1:
                fps_text = font.render(f"FPS: " + str(math.trunc(clock.get_fps())), True, (255,255,255))
                window.blit(fps_text, (0,120))


        # Render Menu sections
            for i in range(len(items)):
                if i == selected_section:
                    menu_text = menu_font.render(items[i],0, CYAN)
                else:
                    menu_text = menu_font.render(items[i],0, DARK_CYAN)
                menu_text_rect = menu_text.get_rect(center = ( menuX, 250+ menu_spacing * i))
                window.blit(menu_text, menu_text_rect)

        # Splashes
            if SPLASHES == 1:
                window.blit(splash_text, (WIDTH // 2.7, HEIGHT // 170)) 

        # Debug Func (Shows selected Window Mode on the screen).
            if DEBUG_MODE == 1:
                if WINDOW_MODE == 2:
                    window.blit(fullscreen_text,(0,90))
                if WINDOW_MODE == 1:
                    window.blit(resizable_text, (0,90))
                if WINDOW_MODE == 3:
                    window.blit(hardware_render_text, (0,90))
                if WINDOW_MODE == 0:
                    window.blit(default_window_text, (0,90))

            # Menu section start scrolling animation.
                menuX += menu_speed
                menu_spacing += 2.2            
                if menuX > 100:
                    menu_speed -= 0.21
                    if menu_speed < -0:
                        menu_speed = -0
                if menu_spacing > 74:
                    menu_spacing = 74


        # Update screen
            pygame.display.update()
            clock.tick(FPS)

def Level_Select():
    if MUSIC == 1:
        LevelSelectMusic()

    global running
    while running:

       # Quit Event
        for e in pygame.event.get():
            if e.type == pygame.QUIT:

                running = False
                pygame.quit()
                sys.exit()

        # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    sys.exit()

        # 'BACKSPACE' Key to back in menu
            if e.type == pygame.KEYUP:
                if e.key == back_keyboard:
                    running = False
                    switch_scene(MainMenu)
                    if SFX == 1:
                        click2Sound.play()

            window.fill((117, 25, 25))
            window.blit(level_select_title_text, (0,0))

        # Update screen
        pygame.display.update()
        clock.tick(FPS)



            
def Level_1():
    global running, character_y, character_x, character_speed, WINDOW_MODE, window
    while running:

       # Quit Event
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                mainLoadingScreen()
                running = False
                pygame.quit()
                sys.exit()

        # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == quit_from_game_keyboard:
                    mainLoadingScreen()
                    running = False
                    pygame.quit()
                    sys.exit()

            # Switch to fullscreen mode (ALT + ENTER)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and (keys[pygame.K_LALT] or keys[pygame.K_RALT]):
                    mainLoadingScreen()
                    toggle_fullscreen()

        # 'BACKSPACE' Key to back in menu
            if e.type == pygame.KEYUP:
                if e.key == back_keyboard:
                    switch_scene(MainMenu)
                    if SFX == 1:
                        click2Sound.play()
                    running = False

    # --- Player Controls ----

        # --- Keyboard controls ----
        if CONTROLS == 1:

            keys = pygame.key.get_pressed()
                
            if keys[player_run_keyboard]:
                character_speed = 10
            else:
                character_speed = 5
                
            if keys[player_go_left_keyboard]:
                character_x -= character_speed

            if keys[player_go_right_keyboard]:
                character_x += character_speed

        # ---- Controller controls ----

        # XBOX 360 Controls.
        if CONTROLS == 2: 

            if joystick.get_button(1): 
                if GAMEPAD_VIBRATION == 1:
                    joystick.rumble(0.5, 0.5, 10) # Controller rumble (or vibration).

            # Player movement (Controller).
            left_stick_x = joystick.get_axis(left_analog_stick_axis_xbox360)

            character_x += left_stick_x * character_speed

        # Player speed (Controller).
            if joystick.get_button(player_run_xbox360):
                character_speed = 10
            else:
                character_speed = 5

        # Render images           
        window.fill((82, 212, 255))
        window.blit(build_info_text, (0,0))
        window.blit(door1, (1000,100))
        window.blit(character_img,(character_x, character_y))
        window.blit(grass_img, (-100,500))

        # Update screen
        pygame.display.update()
        clock.tick(FPS)

    fade_in(1280,720) # Fade in.


# Switch scene
switch_scene(MainMenu)
while current_scene is not None:
    current_scene()

