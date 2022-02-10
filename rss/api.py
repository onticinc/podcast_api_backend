import http.client

conn = http.client.HTTPSConnection("api.simplecast.com")
payload = ''
headers = {}
conn.request("GET", "/episodes/8d60a36a-8830-4d05-af67-e6e1667a0741", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))