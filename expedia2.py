import md5
import time
import urllib2
import httplib
httplib.HTTPConnection.debuglevel = 1




customerUserAgent="""OpenAnything/1.0 +http://diveintopython.org/"""
service = 'http://api.ean.com/ean-services/rs/hotel/'
version = 'v3/'
method = 'list/'
hotelId = '201252'
destinationString='paris'
otherElementsStr = '&cid=55505&minorRev=23&customerIpAddress=127.0.0.1&locale=en_EN&currencyCode=USD&countryCode=FR' 

apiKey = '64ijnglbl4v7bso914mfpuqg9s'
secret = '979iimo4lcdep'

hash = md5.new()
# seconds since GMT Epoch
timestamp = str(int(time.time()))
# print timestamp
sig = md5.new(apiKey + secret + timestamp).hexdigest()
print len(sig)
url = service + version + method+ '?apiKey=' + apiKey + '&sig=' + sig + otherElementsStr +'&destinationString=' + destinationString
#'&hotelIdList=' + hotelId
print url

request = urllib2.Request(url)
request.add_header('customerUserAgent', 'OpenAnything/1.0 +http://diveintopython.org/')
opener = urllib2.build_opener()
feeddata = opener.open(request).read()
print(feeddata)