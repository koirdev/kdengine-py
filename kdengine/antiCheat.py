import pymem
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
pm = pymem.Pymem()
ProcessName = "cheatengine-x86_64-SSE4-AVX2.exe"

def close():
    print("test")
    pass



def checkGame():
	#If OS/Platform is Windows (ONLY for Windows).
	try:
		pm.open_process_from_name(ProcessName) # Searching for 'Discord.exe' process.
		print(f"{ProcessName} founded.")
		sysCrash()
	except pymem.exception.ProcessNotFound: #If process 'Discord.exe' was not found (For Windows).
		print(f"The {ProcessName} process was not found.")



