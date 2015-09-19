import json, requests

url='https://maps.googleapis.com/maps/api/elevation/json?locations=43.296950,5.381070'
response = requests.get(url)
#print response.status_code
data = json.loads(response.text)
print data['results'][0]['elevation']