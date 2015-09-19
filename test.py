import unirest
response = unirest.get("https://zilyo.p.mashape.com/search?latitude=52.5306438&longitude=13.3830683",
  headers={
    "X-Mashape-Key": "tRYCmIgZPTmshlgBDyltncD8g4Cdp1IYcmGjsnccRZfWHlrAU7",
    "Accept": "application/json"
  }
  )
print response.code
print response.body