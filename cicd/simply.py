import requests
import json
import os
import sys


def iics_login(URL,username,password):
	headers = {'content-type':'application/json'}
	data = {"username":username,"password":password}

	response=requests.post(url=URL, data=json.dumps(data), headers=headers)

	if response.status_code != 200:
		print("unable to login - " + response.text)
		return 99
	else:
		print("Login Successful")
		jresponse=response.json()
		return jresponse["userInfo"]["sessionId"]
    

def iics_logout(URL,sessionId):
	headers = {'content-type':'application/json', 'INFA-SESSION-ID':sessionId}

	response=requests.post(url=URL, headers=headers)
	if response.status_code != 200:
		print("unable to logout - " + response.text)
		return 99
	else:
		print("Logout Successful")
		return 0

iics_user_name = os.environ['IICS_USER_NAME']

sessionId = iics_login('https://dm-ap.informaticacloud.com/ma/api/v3/InternalLogin',iics_user_name,'Simplya!@789')
print("Session ID - " + sessionId)
	
iics_logout('https://dm-ap.informaticacloud.com/saas/public/core/v3/logout',sessionId)

