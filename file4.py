import phonenumbers
import geocoder
from phonenumbers import carrier,geocoder,timezone
phone_number=input("enter your phonenumber")
parse=phonenumbers.parse(phone_number)
location=geocoder.description_for_number(parse,"en")
print("my location is",location)
carrier=carrier.name_for_number(parse,"en")
print("my carrier is",carrier)
timezone=timezone.time_zones_for_number(parse)
print("my time_zone is",timezone)


