import json, requests

print "----------------------------------------------------"
#places textsearch
#url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=beach+Marseille&key=AIzaSyDO0zcbNxDysY2GFj4RecvWVAoUuxvOc0Q'


#beach is the keyword to look for beach and look for natural_feature in types to confirm
#places nearby search
url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=43.296950,5.381070&radius=20000&key=AIzaSyDO0zcbNxDysY2GFj4RecvWVAoUuxvOc0Q&keyword=surf'

response = requests.get(url)
#print response.status_code
data = json.loads(response.text)
#for i in range(5):
#	for key in data['results'][i].keys():
#		print key, data['results'][i][key]

#for key in data['results'][0].keys():
#		print key, data['results'][0][key]

#typo should be natural_feature
#for typo in data['results'][0]['types']:
#	print typo

#print data['results'][0]

place_id=data['results'][0]['place_id']


#place details
url='https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyDO0zcbNxDysY2GFj4RecvWVAoUuxvOc0Q&placeid=' + place_id
response = requests.get(url)
data = json.loads(response.text)
#print data
for key in data['result'].keys():
	print key, data['result'][key]

print 'name %s' %data['result']['name']
print 'number of user ratings %d' %data['result']['user_ratings_total']
print 'phone no %s' %data['result']['international_phone_number']
print 'lat %s' %data['result']['geometry']['location']['lat']
print 'lng %s' %data['result']['geometry']['location']['lng']