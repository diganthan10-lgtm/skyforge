import numpy as np
import matplotlib.pyplot as plt

from aircraft import cl_max

# Thin airfoil theory: CL = 2*pi*alpha (alpha in radians)
alpha_deg = np.linspace(-5, 15, 200)
alpha_rad = np.radians(alpha_deg)

cl_ideal = 2 * np.pi * alpha_rad

# Clip at the max lift coefficient to show stall
cl = np.minimum(cl_ideal, cl_max)

# Zero-lift angle is 0 for a symmetric airfoil; print lift slope for reference
print(f"Lift slope: {2 * np.pi:.2f} per radian ({2 * np.pi / 57.3:.3f} per degree)")

plt.figure(figsize=(8, 5))
plt.plot(alpha_deg, cl, label="Thin airfoil, clipped at CL,max")
plt.plot(alpha_deg, cl_ideal, "--", color="gray", label="Thin airfoil, unclipped")
plt.axhline(cl_max, color="red", linewidth=0.8, label=f"CL,max = {cl_max}")
plt.xlabel("Angle of attack (deg)")
plt.ylabel("Lift coefficient CL")
plt.title("skyforge: lift vs angle of attack")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
