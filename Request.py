import requests

a = requests.get(url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
             params={'api_key': 'MbNWQfHAsg9gatULkp04nACdeqPBrJqihYNQSEWo', 'earth_date': '2022-05-25'})

resp = a.json()

ph = resp['photos']
print(*[i['img_src'] for i in ph][:3], sep='\n')
