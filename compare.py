import numpy as np

from aircraft import rho, g

# Approximate specs (verify against manufacturer data before relying on these)
# name: (max takeoff weight kg, wing area m^2, max lift coefficient with flaps)
aircraft = {
    "Cessna 172":  (1157, 16.2, 2.0),
    "Piper Cub":   (862,  15.8, 1.9),
    "skyforge":    (1000, 16.0, 1.5),
}

print(f"{'Aircraft':<12}{'Weight (kg)':>12}{'Wing (m^2)':>12}{'Stall (kts)':>13}")
for name, (mass, area, cl_max) in aircraft.items():
    v_stall = np.sqrt(2 * mass * g / (rho * area * cl_max))  # m/s
    print(f"{name:<12}{mass:>12.0f}{area:>12.1f}{v_stall * 1.944:>13.0f}")
