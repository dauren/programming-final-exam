import requests

yahooql = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='Almaty') and u='c'"
url = "https://query.yahooapis.com/v1/public/yql?q=%s&format=json" % yahooql
r = requests.get(url)
data = r.json()
#continue your code
