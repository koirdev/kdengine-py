from config import *

# Logging.
if LOGGING == 1:
	import os, sys, logging, traceback
	from logging.handlers import RotatingFileHandler
	open(LOG_FILE_NAME, 'w').close()
	log = os.path.join(os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.getcwd(), LOG_FILE_NAME)
	logging.basicConfig(filename=log, level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s",datefmt='%Y-%m-%d %H:%M:%S')
	sys.stdout = open(log, "a", buffering=1)
	sys.stderr = open(log, "a", buffering=1)

print("Loading KD Engine...")

from antiCheat import *
from checkFiles import *
from server_client import *
from os_info import *
from graphics_loader import *
from openLinks import *
from message_box import *
from splashes import *
from sound_loader import *
from discord_api import *
from urlDownloadContent import *
from zipExtractor import *
from classes import *
from controls.keyboard_config import *
from controls.xbox360_config import *

#from localhost_server.server import * - server test stuff...










