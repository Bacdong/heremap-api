import requests
import json

print('Enter address: ')
keyword = input()

apikey = 'RQl3iAyScjF6OlVJsAMz4UdtQ0e-e7hSG5fF9xpbPDs';
api_url = 'https://geocode.search.hereapi.com/v1/geocode?q=%s&apiKey=%s' % (keyword, apikey, )

res = requests.get(api_url)
data = res.json()

if not data:
    response = {
        'message': 'Address not found',
        'status': False,
    }
else:
    items = data['items']

    for item in items:
        title = item['title']
        position = item['position']
        lat = position.get('lat')
        lng = position.get('lng')

    response = {
        'title': title,
        'lat': lat,
        'lng': lng,
    }

print(response)

