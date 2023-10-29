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


print("Reading command line values")
print(sys.argv)

VAR0="".join(sys.argv[0:])
VAR1="".join(sys.argv[1:])
VAR2="".join(sys.argv[2:])
print(VAR0 + " - "VAR1 + " - " + VAR2)



iics_user_name = os.environ['IICS_USER_NAME']
iics_password = os.environ['IICS_PASSWORD']
iics_login_url = os.environ['IICS_LOGIN_URL']
iics_logout_url = os.environ['IICS_LOGOUT_URL']

print("login-url: " + iics_login_url)
print("logout-url: " + iics_logout_url)




sessionId = iics_login(iics_login_url,iics_user_name,iics_password)
print("Session ID - " + sessionId)
	
iics_logout(iics_logout_url,sessionId)

