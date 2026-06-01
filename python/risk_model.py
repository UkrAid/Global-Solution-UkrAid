#Imports:
import math

#K_ Consts:
# Threat attenuation constants
K_TROOPS = 0.001      # persistent, mobile threat
K_AIR_RAID = 0.003    # wide area, temporary  
K_MISSILE_MAX = 0.005 # highest risk per distance unit

#Functions:
def haversine(lat1, lon1, lat2, lon2):
    r = 6371 #This is earth's radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    return 2 * r * math.asin(math.sqrt(a))


def troop_risk(d, k = K_TROOPS):
    return math.exp(-k * d) / (d ** 2)


def air_raid_risk(d, k = K_AIR_RAID):
    return math.exp(-k* d) / (d ** 2)

def missile_strike(d, k = K_MISSILE_MAX):
    return math.exp(-k* d) / (d ** 2)

def total_risk(r_missile, r_air, r_troops):
    return max(r_missile, r_air, r_troops)

def risk_label(risk):
    if risk > 0.001:
        return f"[ALERT!] Critical risk of: {risk:.4f}"
    if risk > 0.0001:
        return f"[ALERT!] High risk of :{risk:.4f}"
    if risk > 0.00001:
        return f"Moderate risk of :{risk:.4f}"
    else:
        return "Low Distance-Based Risk"