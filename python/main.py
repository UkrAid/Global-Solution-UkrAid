#Imports:
from pyfiglet import figlet_format
from risk_model import troop_risk, air_raid_risk, missile_strike, total_risk



#Func de apoio:
def println(str_):
    print(str_, "\n")

def separador():
    print("═" * 53 + "\n")

def pause():
    input("Press enter to return...\n")




#Main func:
def main():
     usr_lat = None
     usr_lon = None

     separador()
     print(figlet_format("OrbitGuard"))
     while True:
          separador()
          print("""
          [1] About this system
          [2] Troop Movement tracker
          [3] Air raid alert monitor
          [4] Safe route calculator
          [5] Refugee resource locator
          [0] Exit
          """ + "\n")

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
                         if usr_lat is None or usr_lon is None: 
                              usr_lat = float(input("Insert your latitue: E.g. -23.5505 | "))
                              usr_lon = float(input("Insert your longitude: E.g. 74.0060 | "))
                         else:
                              print("case 2")
                              break
                    except ValueError:
                         println("Invalid input - please enter a valid coordinate. E.g. -23.5505")
                         pause()


               case "3":
                    try:
                         if usr_lat is None or usr_lon is None: 
                              usr_lat = float(input("Insert your latitue: E.g. -23.5505 | "))
                              usr_lon = float(input("Insert your longitude: E.g. 74.0060 | "))
                         else:
                              print("case 3")
                              break
                    except ValueError:
                         println("Invalid input - please enter a valid coordinate. E.g. -23.5505")
                         pause()


               case "4":
                    try:
                         if usr_lat is None or usr_lon is None: 
                              usr_lat = float(input("Insert your latitue: E.g. -23.5505 | "))
                              usr_lon = float(input("Insert your longitude: E.g. 74.0060 | "))
                         else:
                              print("case 4")
                              break
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