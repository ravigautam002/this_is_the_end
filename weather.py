import json, requests, datetime

url='https://api.forecast.io/forecast/b08f0624949b72ccda46eb99702ef6f2/48.866667,2.333333,2015-08-30T00:00:00+0200?units=si'
response = requests.get(url)
print response.status_code
data = json.loads(response.text)
#for key in data.keys():
#	print key

#possible icon values - clear-day, clear-night, rain, snow, sleet, wind, fog, cloudy, partly-cloudy-day, or partly-cloudy-night. (Developers should ensure that a sensible default is defined, as additional values, such as hail, thunderstorm, or tornado, may be defined in the future.)
#lattitude and longitude through google geocoding api
#integrate confidence in prediction later
#issues with gmt and timezones google timezone api
#issues with past dates
print data['daily']['data'][0]['icon']
print 'max'
print data['daily']['data'][0]['apparentTemperatureMax']
print 'min'
print data['daily']['data'][0]['apparentTemperatureMin']
print 'speed m/s'
print data['daily']['data'][0]['windSpeed']
print 'summary'
print data['daily']['data'][0]['summary']
print 'time'
print data['daily']['data'][0]['time']
print(
    datetime.datetime.fromtimestamp(
        int(data['daily']['data'][0]['time'])
    ).strftime('%Y-%m-%d %H:%M:%S')
)
print 'timezone'
print data['timezone']
print 'offset'
print data['offset']
print data['daily']
#alert objects, see documentation