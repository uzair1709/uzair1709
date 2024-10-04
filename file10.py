import requests
def get_location(ip_address):
   response=requests.get(f"http://ip-api.com/json/{ip_address}")
   data=response.json()
   return data
ip_address=("80.76.173.91")
win=get_location(ip_address)
print(f"country:{win["country"]}")
print(f"city:{win["city"]}")
print(f"timezone:{win["timezone"]}")
print(f"region:{win["region"]}")
print(f"query:{win["query"]}")
print(f"as:{win["as"]}")
print(f"offset:{win["offset"]}")