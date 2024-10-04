import requests
def get_location(ip_address):
    response=requests.get(f"http://ip-api.com/json/{ip_address}")
    data=response.json()
    return data
ip_address="37.186.36.25"
location=get_location(ip_address)
print(f"country:{location["country"]}")
