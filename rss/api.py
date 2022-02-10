import http.client

conn = http.client.HTTPSConnection("api.simplecast.com")
payload = ''
headers = {}
conn.request("GET", "/episodes/eyJhcGlfa2V5IjoiZjliNTUzZjg5MTEwYmIyOWNkMzZmOTQwYTFkMjZlYjkifQ==", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))