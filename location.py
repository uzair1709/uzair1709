import phonenumbers
from phonenumbers import geocoder
import webbrowser
def get_location_from_number(phone_number):
    try:
        parsed_number=phonenumbers.parse(phone_number)
        locaton_description=geocoder.description_for_number(parsed_number,"en")
        if locaton_description:
            return locaton_description
        else:
            print("could not find the location foe given number") 
            return None
    except phonenumbers.NumberParseException:
        print("invalid phone number format")
        return None
uzair=input("enter your phone number with your country code")
location=get_location_from_number(uzair)
if location:
    google_map_url=f"https://www.google.com/maps/search/?api=1&query={location.replace(" ","+")}"
    webbrowser.open(google_map_url)
    print(f"openings app for location:{location}")