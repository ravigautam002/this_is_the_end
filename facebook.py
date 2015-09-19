import urllib2
import httplib
httplib.HTTPConnection.debuglevel = 1

access_token="""CAACEdEose0cBAMgGqICDYgu5lO8C8FbCK4jTuFIWpNnuAfasA7BtY3ZBjhXxxTOFNZBrTqyBZBzw3K1PXImfNrn8HLZBjItaPCjjWWPr1EKZAXMU9wOsmxAtvSBIiwmSfc3y3d8xwG7paWFFWMKOlNv2JPViDaZB2hHogYkDvN7GdZCXByBDKkZBwx94G6V3g7JR0XkCxR54f8Y1zacMPsYr6M2sfPKqTMAZD"""
url='https://graph.facebook.com/v2.3/me/?access_token=' + access_token + '&fields=id,name,birthday,posts'
#print(url)

request = urllib2.Request(url)
opener = urllib2.build_opener()
feeddata = opener.open(request).read()
print(feeddata)