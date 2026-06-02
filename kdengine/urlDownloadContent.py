import requests, sys, os
from zipExtractor import *
from message_box import *
from config import url

responce = requests.get(url)

def downloadAssetsFromURL():
	try:
		print(f"Downloading resources from: {url} - URL") 
		local_file_name = "assets.zip" # Set a custom name for downloaded file.

		with open(local_file_name, "wb") as f:
			f.write(responce.content)
			print(f"Done, downloaded in:", local_file_name)
			responce.close() # Closes after downloading file.
			ExtractZIPAssets() # Runs ZIP Extractor for unziping the downloaded file.

	# ---- Excepts -----

	# requests.RequestException - A Connection error occurred.
	except requests.RequestException:
		print("requests.RequestException - A Connection error occurred.")
		URLRequestExceptionError()
		sys.exit()

	# requests.ConnectionError - There was an ambiguous exception that occurred while handling your request.
	except requests.ConnectionError:
		print("requests.ConnectionError - There was an ambiguous exception that occurred while handling your request.")
		URLConnectionError()
		sys.exit()

	# requests.HTTPError - An HTTP error occurred.
	except requests.HTTPError:
		print("requests.HTTPError - An HTTP error occurred.")
		URLHTTPError()
		sys.exit()

	# requests.TooManyRedirects - Too many redirects.
	except requests.TooManyRedirects:
		print("requests.TooManyRedirects - Too many redirects.")
		URLTooManyRedirectsError()
		sys.exit()

	# requests.ConnectTimeout - The request timed out while trying to connect to the remote server.
	except requests.ConnectTimeout:
		print("requests.ConnectTimeout - The request timed out while trying to connect to the remote server.")
		URLConnectTimeoutError()
		sys.exit()

	# requests.ReadTimeout - The server did not send any data in the allotted amount of time.
	except requests.ReadTimeout:
		print("requests.ReadTimeout - The server did not send any data in the allotted amount of time.")
		URLReadTimeoutError()
		sys.exit()

	# requests.Timeout - The request timed out.
	except requests.Timeout:
		print("requests.Timeout - The request timed out.")
		URLTimeoutError()
		sys.exit()

	# requests.JSONDecodeError - Couldn’t decode the text into json.
	except requests.JSONDecodeError:
		print("requests.JSONDecodeError - Couldn’t decode the text into json.")
		URLJSONDecodeError()
		sys.exit()




