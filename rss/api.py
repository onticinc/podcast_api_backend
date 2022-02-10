authorization: Bearer {token}


import requests


response = requests.get('https://api.simplecast.com')


# response_dict = response.json()

print(response)