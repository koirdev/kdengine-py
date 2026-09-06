import zipfile, os, sys
from message_box import *
from pathlib import Path

def ExtractZIPAssets():
	fileName = (Path(__file__).name)
	try:
		extractDir = "" # Directory for unziping the archive.
		archiveDir = "assets.zip" # Archive's directory.
		print(f"'{fileName}' - Archive directory:", '{archiveDir}', "\nExtract directory:", extractDir)	
		with zipfile.ZipFile(archiveDir, 'r') as zip_file: # Unziping.
			print(f"'{fileName}' - Extracting ZIP archive...")
			zip_file.extractall(extractDir)
			print(f"'{fileName}' - Done")
			zip_file.close() # Closes after unziping.
			#print("Deleting the ZIP archive...")
			#deletePath = "../assets.zip"
			#os.remove(archiveDir)
			#print("Done")

	# ---- Excepts -----

	# zipfile.BadZipFile - Bad ZIP file.
	except zipfile.BadZipFile:
		print(f"'{fileName}' - zipfile.BadZipFile - Bad ZIP file.")
		ZIPBadFileZipFileError()
		sys.exit()

	# zipfile.LargeZipFile - Large ZIP file.
	except zipfile.LargeZipFile:
		print(f"'{fileName}' - zipfile.LargeZipFile - Large ZIP file.")
		ZIPLargeZipFileError()
		sys.exit()

