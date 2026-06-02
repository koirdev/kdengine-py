import zipfile, os, sys
from message_box import *


def ExtractZIPAssets():
	try:
		extractDir = "" # Directory for unziping the archive.
		archiveDir = "assets.zip" # Archive's directory.
		print(f"Archive directory:", archiveDir, "\nExtract directory:", extractDir)	
		with zipfile.ZipFile(archiveDir, 'r') as zip_file: # Unziping.
			print("Extracting ZIP archive...")
			zip_file.extractall(extractDir)
			print("Done")
			zip_file.close() # Closes after unziping.
			#print("Deleting the ZIP archive...")
			#deletePath = "../assets.zip"
			#os.remove(archiveDir)
			#print("Done")

	# ---- Excepts -----

	# zipfile.BadZipFile - Bad ZIP file.
	except zipfile.BadZipFile:
		print("zipfile.BadZipFile - Bad ZIP file.")
		ZIPBadFileZipFileError()
		sys.exit()

	# zipfile.LargeZipFile - Large ZIP file.
	except zipfile.LargeZipFile:
		print("zipfile.LargeZipFile - Large ZIP file.")
		ZIPLargeZipFileError()
		sys.exit()

