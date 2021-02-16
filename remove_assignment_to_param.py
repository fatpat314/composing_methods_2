# By Kami Bigdely
# Remove assignment to method parameter.
class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
class Mass:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

def calculate_kinetic_energy(mass, distance, time):
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit        
            in_km = distance.value * 9.461e12
            calculated_distance = Distance(in_km, "km") 
        else:
            print ("unit is Unknown")
            return
    speed = calculated_distance.value/time # [km per sec]

    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            calculated_mass = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return    
        
    kinetic_energy = 0.5 * calculated_mass.value * speed ** 2
    return kinetic_energy

calculated_distance = Distance(2, 'ly')
calculated_mass = Mass(2, "solar-mass")
print(calculate_kinetic_energy(calculated_distance, calculated_mass, 3600e20))