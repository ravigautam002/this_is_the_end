import json, requests

print "----------------------------------------------------"

url='https://api.foursquare.com/v2/venues/explore?client_id=SAQU5SKZVPUNF5LCLXIRDPWFEPRIG10NPNQSN3X1PORC03OJ&client_secret=AWC4KEPFJAPPQJFIS3BS5SWWQE33ETBOXY0RRO04PCPDXSO4&v=20140806&m=foursquare&ll=43.29,5.38&query=museum'

response = requests.get(url)
#print response.status_code
data = json.loads(response.text)

print data
