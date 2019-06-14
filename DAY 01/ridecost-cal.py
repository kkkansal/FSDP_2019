
travel_km = float(input("Enter the kilometer: "))
diesel_cost = 80.0
vehicle_fuel_avg = 18.0
fuel_consumption = (travel_km/vehicle_fuel_avg)
cost = (diesel_cost*fuel_consumption)
print ("Cost of driving  :"+str(round(cost,2))+" Rs")