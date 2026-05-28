"""
Raul Azzi Corsi
RM569022
Global Solution 2026 - Semestre 1
"""


#Imports:
from pyfiglet import figlet_format
from risk_model import troop_risk, air_raid_risk, missile_strike, total_risk, haversine
from api import get_token, get_conflicts_events, get_country
from support_functions import println, pause, separador, separador_up, separador_down
from dotenv import load_dotenv
import os

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


     separador_up()
     print(figlet_format("OrbitGuard"))
     separador_down()

     while True:
          print("""
          [1] About this system
          [2] Distance Based Risk
          [3] Air raid alert monitor
          [4] Safe route calculator
          [5] Refugee resource locator
          [0] Exit
          """)

          separador()

          usr_choice = input("Insert choice: ")
          match usr_choice:
               case "1":
                    separador()
                    print("""   ABOUT ORBITGUARD
                          
   OrbitGuard is a cli application that aims to 
   centralize all OSINT available data inside the 
   territory of Ukraine in order to help civilians 
   to find resources, safe zones and to alert of 
   any danger in the horizon.
                          """)
                    separador()
                    pause()


               case "2":
                    try:
                         if usr_lat is None or usr_lon is None:                                #Ukraine
                              usr_lat = float(input("Insert your latitue: E.g. -23.5505 | "))  #50.4501
                              usr_lon = float(input("Insert your longitude: E.g. 74.0060 | ")) #30.5234
                              usr_country = get_country(usr_lat, usr_lon)
                         
                         events = get_conflicts_events(token, usr_country, limit=3)
                         for i in events:
                              d = haversine(usr_lat, usr_lon, float(i["latitude"]), float(i["longitude"]))
                              risk = troop_risk(d)

                              print(
                                   "\n",
                                   i["event_date"], 
                                   i["event_type"], 
                                   i["latitude"], 
                                   i["longitude"], 
                                   i["location"],
                                   i["fatalities"],
                              )
                              println(f" Risk vector is: {risk}.") 
                              separador()



                    except ValueError:
                         println("Invalid input - please enter a valid coordinate. E.g. -23.5505")
                         pause()

                    


               case "3":
                    
                    try:
                         
                         print("case 3")

                    except:
                         println("Could not reach alert service. Check your connection.")
                         pause()



               case "4":
                    dst_lat = None
                    dst_lon = None

                    try:
                         if usr_lat is None or usr_lon is None: 
                              usr_lat = float(input("Insert your latitue: E.g. -23.5505 | "))
                              usr_lon = float(input("Insert your longitude: E.g. 74.0060 | "))
                         
                         dst_lat = float(input("Insert destination latitue: E.g.  50.4501 | "))
                         dst_lon = float(input("Insert destination's longitude: E.g.  30.5234 | "))
                         
                    
                    except ValueError:
                         println("Invalid input - please enter a valid coordinate. E.g. -23.5505")
                         pause()


               case "5":
                    try:
                         if usr_lat is None or usr_lon is None: 
                              usr_lat = float(input("Insert your latitue: E.g. -23.5505 | "))
                              usr_lon = float(input("Insert your longitude: E.g. 74.0060 | "))
                         else:
                              print("case 5")
                              break
                    except ValueError:
                         println("Invalid input - please enter a valid coordinate. E.g. -23.5505")
                         pause()

          
               case "0":
                    break
               case _:
                    println("Wrong input type.")
                

if __name__=="__main__":
    main()