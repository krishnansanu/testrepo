import requests
import json


def my_func(URL,username,password):
	headers = {'content-type':'application/json'}
	data = {"username":username,"password":password}
	print("URL - " + URL)
	print(headers)
	print(data)
    
	response=requests.post(url=URL, data=json.dumps(data), headers=headers)

	if response.status_code != 200:
		print("unable to login - " + response.text)
		return 99
	else:
		jresponse=response.json()
		return jresponse["userInfo"]["sessionId"]
    

sessID = my_func('https://dm-ap.informaticacloud.com/ma/api/v3/InternalLogin','Krishnan.Ravi.uat2','Simplya!@789')
print("Session ID - " + sessID)
	


#URL = 'https://www.w3schools.com/python/demopage.php'
#myobj = {'somekey': 'somevalue'}
#x = requests.post(url=URL, json = myobj)
#print the response text (the content of the requested file):


