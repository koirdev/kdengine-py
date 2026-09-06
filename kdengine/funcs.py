# in dev

from pathlib import Path

printL = None
def logPrint(printL):
	

	fileName = (Path(__file__).name)
	print(filename + printL)

logPrint()