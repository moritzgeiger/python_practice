def ground_shipping(weight):
  flat_charge = 20
  if weight <= 2:
    return flat_charge + 1.5 * weight
  elif weight <= 6:
    return flat_charge + 3 * weight
  elif weight <= 10:
    return flat_charge + 4 * weight
  elif weight > 10:
    return flat_charge + 4.75 * weight
  
p_ground_shipping = 125

#print(ground_shipping(5))

def drone_shipping(weight):
  if weight <= 2:
    return 4.5 * weight
  elif weight <= 6:
    return  9 * weight
  elif weight <= 10:
    return 12 * weight
  elif weight > 10:
    return 14.25 * weight


#print(drone_shipping(5))

def cheapest_fare(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = p_ground_shipping
  if ground < drone and  ground < premium:
    method = "Ground Shipping"
    cost = ground
  if premium < drone and  premium < ground:
    method = "Premium Shipping"
    cost = premium
  if drone < premium and  drone < ground:
    method = "Drone Shipping"
    cost = drone
  print("Shipping by " + method + " is cheapest." + " The total costs are: "+ str(cost) + ".")

cheapest_fare(41.5)