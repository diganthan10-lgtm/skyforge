import numpy as np

from aircraft import mass, wing_area, cd0, k, rho, g

# Best glide happens where drag is minimized: CL = sqrt(CD0 / k)
cl_best = np.sqrt(cd0 / k)
cd_best = cd0 + k * cl_best**2
glide_ratio = cl_best / cd_best

# Speed for best glide, from L = W at that CL
v_best = np.sqrt(2 * mass * g / (rho * wing_area * cl_best))

altitude = 1000.0  # m, starting height for the glide
glide_distance = glide_ratio * altitude

print(f"Best lift coefficient: {cl_best:.3f}")
print(f"Best glide ratio (L/D): {glide_ratio:.1f}")
print(f"Speed for best glide: {v_best:.1f} m/s ({v_best * 1.944:.0f} knots)")
print(f"Glide distance from {altitude:.0f} m: {glide_distance / 1000:.1f} km")
