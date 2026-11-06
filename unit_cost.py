# Charter unit cost model: cost per flight hour and break-even ticket price
# All costs are rough placeholder values. Replace them with real quotes.

fuel_burn_gph = 9.0        # gallons per hour, typical for a 4-seat single
fuel_price = 5.50          # $ per gallon
maintenance_per_hr = 80.0  # $ per flight hour
insurance_per_yr = 6000.0  # $ per year
annual_hours = 200.0       # hours flown per year
fixed_per_yr = 12000.0     # hangar, training, misc. $ per year
seats = 4
load_factor = 0.5          # average fraction of seats sold

fuel_per_hr = fuel_burn_gph * fuel_price
annual_fixed = insurance_per_yr + fixed_per_yr
cost_per_hr = fuel_per_hr + maintenance_per_hr + annual_fixed / annual_hours

seats_sold = seats * load_factor
breakeven_per_seat = cost_per_hr / seats_sold

print(f"Fuel cost per hour: ${fuel_per_hr:,.0f}")
print(f"Total cost per flight hour: ${cost_per_hr:,.0f}")
print(f"Break-even price per seat (1 hr flight): ${breakeven_per_seat:,.0f}")
