import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
referrer = input("[#] Enter the WARP+ ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear') 
		print(f"[#] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		animation = ["[5%]","[10%]","[15%]","[20%]","[25%]","[30%]","[35%]","[40%]","[45%]","[50%]","[55%]","[60%]","[65%]","[70%]","[75%]","[80%]","[85%]","[90%]","[95%]","[100%]"] 
		for i in range(len(animation)):
			time.sleep(1)
			sys.stdout.write("\r[+] Re-Inject... " + animation[i % len(animation)])
			sys.stdout.flush()
	else:
		run()
