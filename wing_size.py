import numpy as np

from aircraft import mass, rho, g
cl_takeoff = 1.2     # takeoff lift coefficient (flaps assumed)
v_takeoff_kts = 45   # target takeoff speed, knots

v_takeoff = v_takeoff_kts / 1.944  # convert knots to m/s

# From L = W: 0.5 * rho * V^2 * S * CL = m * g, solve for S
wing_area = (2 * mass * g) / (rho * v_takeoff**2 * cl_takeoff)

# Wing loading and span for a chosen aspect ratio
aspect_ratio = 7.0
span = np.sqrt(wing_area * aspect_ratio)
chord = wing_area / span

print(f"Target takeoff speed: {v_takeoff:.1f} m/s ({v_takeoff_kts} knots)")
print(f"Required wing area: {wing_area:.1f} m^2")
print(f"Wing loading: {mass * g / wing_area:.0f} N/m^2")
print(f"Span (AR {aspect_ratio:.0f}): {span:.1f} m")
print(f"Mean chord: {chord:.2f} m")
