import json, requests

print "----------------------------------------------------"

url='https://maps.googleapis.com/maps/api/geocode/json?address=paris'

response = requests.get(url)
#print response.status_code
data = json.loads(response.text)

#for key in data.keys():
#	print key
#print data['results'][0]

for key in data['results'][0].keys():
	print key, data['results'][0][key]

print data['results'][0]['geometry']['location']