"""
Raul Azzi Corsi
RM569022
Global Solution 2026 - Semestre 1
"""


#Imports:
from pyfiglet import figlet_format
from dotenv import load_dotenv
import os

from api import get_token, get_conflicts_events, get_country, get_nearby_resources, get_facility_name
from risk_model import troop_risk, air_raid_risk, missile_strike, total_risk, haversine, risk_label
from support_functions import println, pause, separador, separador_up, separador_down, clear

#ACLED API Requests:
load_dotenv()
EMAIL = os.getenv("ACLED_EMAIL")
PASSWORD = os.getenv("ACLED_PASSWORD")



#Main func:
def main():
     #Variables:
     usr_lat = None
     usr_lon = None
     usr_country = None

     #APIs:
     token = get_token(os.getenv("ACLED_EMAIL"), os.getenv("ACLED_PASSWORD")) 

     

     while True:
          clear()
          separador_up()
          print(figlet_format("OrbitGuard"))
          separador_down()
          print("""
          [1] About this system
          [2] Distance-Based Risk
          [3] Air raid alert monitor
          [4] Safe route calculator
          [5] Refugee resource locator
          [0] Exit
          """)

          separador()

          usr_choice = input("   Insert choice: ")
          match usr_choice:
               case "1":
                    clear()
                    separador_up()
                    print("""   ABOUT ORBITGUARD
                          
   OrbitGuard is a cli application that aims to 
   centralize all OSINT available data inside the 
   territory of Ukraine in order to help civilians 
   to find resources, safe zones and to alert of 
   any danger in the horizon.
                          """)
                    separador_down()
                    pause()


               case "2":
                    try:
                         if usr_lat is None or usr_lon is None:                                   #Ukraine
                              usr_lat = float(input("   Insert your latitue: E.g. -23.5505 | "))  #50.4501
                              usr_lon = float(input("   Insert your longitude: E.g. 74.0060 | ")) #30.5234
                              print()
                              usr_country = get_country(usr_lat, usr_lon)

                         separador_down()
                         
                         clear()
                         events = get_conflicts_events(token, usr_country, limit=20)
                         events = sorted(events, key=lambda e: haversine(usr_lat, usr_lon, float(e["latitude"]), float(e["longitude"])))
                         events = events[:3]

                         count = 0
                         clear()
                         for i in events:
                              event_type = i["event_type"]
                              d = haversine(usr_lat, usr_lon, float(i["latitude"]), float(i["longitude"]))
                              if event_type == "Battles":
                                   risk = troop_risk(d)
                              elif event_type == "Explosions/Remote violence":
                                   risk = missile_strike(d)
                              
                              if count == 0:
                                   separador_up()

                              print(f"""
 {i["location"]}
 Type:                    {i["event_type"]}
 Date:                    {i["event_date"]}
 Distance:                {d:.1f}km
 Fatalities:              {i["fatalities"]}
 Distance-based risk:     {risk_label(risk)}

"""
)                             #Separa sempre no ultimo evento.
                              if count == len(events) - 1: 
                                   separador_down()
                              
                              count += 1

                         pause()

                    except Exception as e:
                         println(f"   Error: {e}")
                         pause()

                    


               case "3":
                    
                    try:
                         
                         print("case 3")

                    except:
                         println("   Could not reach alert service. Check your connection.")
                         pause()



               case "4":
                    dst_lat = None
                    dst_lon = None

                    try:
                         if usr_lat is None or usr_lon is None: 
                              usr_lat = float(input("   Insert your latitue: E.g. -23.5505 | "))
                              usr_lon = float(input("   Insert your longitude: E.g. 74.0060 | "))
                         
                         dst_lat = float(input("   Insert destination latitue: E.g.  50.4501 | "))
                         dst_lon = float(input("   Insert destination's longitude: E.g.  30.5234 | "))
                         
                    
                    except ValueError:
                         println("Invalid input - please enter a valid coordinate. E.g. -23.5505")
                         pause()


               case "5":
                    try:
                         if usr_lat is None or usr_lon is None:
                              usr_lat = float(input("   Insert your latitude: E.g. 50.4501 | "))
                              usr_lon = float(input("   Insert your longitude: E.g. 30.5234 | "))
                         
                         while True:
                              clear()
                              separador_up()
                              print("""   Refugee Resource Locator:
   [1] Hospitals
   [2] Shelters
   [3] Transport
   [0] Exit
                    """)
                              separador_down()
                              usr_choice_case5 = input("   Insert choice: ")
                              amenity_type = None

                              match usr_choice_case5:
                                   case "1": amenity_type = "hospital"
                                   case "2": amenity_type = "shelter"
                                   case "3": amenity_type = "bus_station"
                                   case "0": break
                                   case _: println("   Please try again")

                              if amenity_type:
                                   amenities = get_nearby_resources(usr_lat, usr_lon, amenity_type)
                                   if amenity_type == "shelter":
                                        amenities = [e for e in amenities if e["tags"].get("shelter_type") != "picnic_shelter"]
                                   amenities = sorted(amenities, key=lambda e: haversine(usr_lat, usr_lon, float(e["lat"]), float(e["lon"])))
                                   amenities = amenities[:3]
                                   clear()
                                   for count, e in enumerate(amenities):
                                        d = haversine(usr_lat, usr_lon, float(e["lat"]), float(e["lon"]))
                                        address = e["tags"].get("addr:street", "")
                                        housenumber = e["tags"].get("addr:housenumber", "")
                                        location = f"{address} {housenumber}".strip() or f"({e['lat']}, {e['lon']})"
                                        if count == 0:
                                             separador_up()
                                        print(f"""
  {get_facility_name(e["tags"], amenity_type)}
  Address:   {location}
  Distance:   {d:.1f}km
  Phone:      {e["tags"].get("phone", "N/A")}
"""
)
                                        if count == len(amenities) - 1:
                                             separador_down()
                                   pause()

                    except Exception as err:
                         println(f"   Error: {err}")
                         pause()

          
               case "0":
                    break
               case _:
                    println("Wrong input type.")
                    pause()
                

if __name__=="__main__":
    main()