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


def get_conflicts_events(token, country, limit=5):
    response = requests.get(
        "https://acleddata.com/api/acled/read?_format=json",
        params={
            "country": country,
            "limit": limit,
            "fields": "event_date|event_type|latitude|longitude|location|fatalities",
            "event_date": "2025-01-01|2026-05-28",
            "event_date_where": "BETWEEN"
        },
        headers={"Authorization": f"Bearer {token}"}
    ) 
    return response.json()["data"]