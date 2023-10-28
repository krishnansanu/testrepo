import requests
import json


def iics_login(username, password):
  URL="https://dm-ap.informaticacloud.com/ma/api/v3/InternalLogin"
  HEADERS = {"content-type":"application/json"}
  BODY = {"username":username,"password":password}

  response=requests.post(url=URL, headers=HEADERS, json=BODY)
  
  if response.status_code != 200:
    print("unable to login -" + response.text)
    return 99
  else:
    print("Login request - Successful")
    json_response=response.json()
    return json["userInfo"]["sessionId"]

def iics_logout(login_url, sessionId):
  HEADERS = {"content-type":"application/json", "INFA-SESSION-ID":sessionId}

  response=requests.post(url=login_url, headers=HEADERS)
  if response.status_code != 200:
    print("unable to logout -" + response.text)
    return 99
  else:
    print("Logout Successful")
    return 0



#Invoking Function
sessID = iics_login("Krishnan.Ravi.uat2","Simplya!@789")
print("SessionID - " + sessID)
