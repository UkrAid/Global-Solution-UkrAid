from dotenv import load_dotenv
import requests
import json


def get_country(lat, lon):
    headers = {"User-Agent": "OrbitGuard/1.0 (Academic Project)"}
    data = requests.get(
        f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en",
        headers=headers
    )
    return data.json()["address"]["country"]
    

def get_token(username, password):
    response = requests.post(
        "https://acleddata.com/oauth/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": "acled",
            "scope": "authenticated"
        }
    )
    return response.json()["access_token"]


def get_conflicts_events(token, country, limit=20, date_from="2025-01-01", date_to="2026-05-29"):
    response = requests.get(
        "https://acleddata.com/api/acled/read?_format=json",
        params={
            "country": country,
            "limit": limit,
            "fields": "event_date|event_type|latitude|longitude|location|fatalities",
            "event_date": f"{date_from}|{date_to}",
            "event_date_where": "BETWEEN"
        },
        headers={"Authorization": f"Bearer {token}"}
    ) 
    return response.json()["data"]

def get_facility_name(tags, amenity_type):
    if amenity_type == "shelter":
        return tags.get("shelter_type", "Emergency Shelter")
    elif amenity_type == "bus_station":
        return tags.get("name:en") or tags.get("name", "Bus Station")
    else:
        return tags.get("name:en") or tags.get("name", "Unknown facility")
    
def get_nearby_resources(lat, lon, amenity_type, radius=100000):
    query = f"""
[out:json];
(
node["amenity"="{amenity_type}"](around:{radius},{lat},{lon});
);
out;
"""
    return requests.get(
        "https://overpass-api.de/api/interpreter",
        params={"data": query},
        headers={"User-Agent": "OrbitGuard/1.0 (Academic Project)"}
    ).json()["elements"]