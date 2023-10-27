import requests
import json


def iics_login(login_url, username, password)
  HEADERS={"content-type":"application/json"}
  BODY={"username":username,"password":password}

  response=requests.post(url=login_url, headers=HEADERS, body=BODY)
  if response.status_code != 200:
    print("unable to login -" + response.text)
    return 99
  else
    print("Login request - Successful")
    json_response=response.json()
    return json["userInfo"]["sessionId"]

def iics_logout(login_url, sessionId)
  HEADERS={"content-type":"application/json", "INFA-SESSION-ID":sessionId}

  response=requests.post(url=login_url, headers=HEADERS)
  if response.status_code != 200:
    print("unable to logout -" + response.text)
    return 99
  else
    print("Logout Successful")
    return 0
