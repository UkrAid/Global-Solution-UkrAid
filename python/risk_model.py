#Imports:
import math


#Functions:
def troop_risk(d, k):
    return math.exp(-k * d) / (d ** 2)


def air_raid_risk(d, k):
    return math.exp(-k * d) / (d ** 2)


def missile_strike(d, t, k_max, lambda_):
    k =  k_max * (1 - math.exp(-lambda_ * t))
    return math.exp(-k * d) / (d ** 2)


def total_risk(r_missile, r_air, r_troops):
    return max(r_missile, r_air, r_troops)