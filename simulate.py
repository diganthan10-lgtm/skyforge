import numpy as np
import matplotlib.pyplot as plt

from aircraft import mass, wing_area, thrust, cd0, k, cl_max, rho as rho0, g
dt = 0.1
t_end = 120.0
steps = int(t_end / dt)

# State: x (distance), h (altitude), v (airspeed), gamma (flight path angle)
x, h, v, gamma = 0.0, 0.0, 0.0, 0.0

time, altitude, speed, aoa = [], [], [], []
takeoff_distance = None

for i in range(steps):
    rho = rho0 * np.exp(-h / 8500)
    q = 0.5 * rho * v**2

    drag = q * wing_area * (cd0 + k * (min(mass * g / (q * wing_area), cl_max))**2) if q > 0 else 0.0

    v_stall = np.sqrt(2 * mass * g / (rho0 * wing_area * cl_max))
    if h <= 0 and v < 1.1 * v_stall:
        gamma = 0.0
        dv = (thrust - drag) / mass
        v += dv * dt
    else:
        if takeoff_distance is None:
            takeoff_distance = x
        gamma = np.radians(10.0)
        dv = (thrust - drag - mass * g * np.sin(gamma)) / mass
        v = max(v + dv * dt, 0.0)
        h += v * np.sin(gamma) * dt
        h = max(h, 0.0)

    x += v * np.cos(gamma) * dt
    time.append(i * dt)
    altitude.append(h)
    speed.append(v)
    aoa.append(np.degrees(gamma))
print(f"Takeoff distance: {takeoff_distance:.0f} m")

fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
axes[0].plot(time, altitude); axes[0].set_ylabel("Altitude (m)")
axes[1].plot(time, speed);    axes[1].set_ylabel("Airspeed (m/s)")
axes[2].plot(time, aoa);      axes[2].set_ylabel("Flight path angle (deg)")
axes[2].set_xlabel("Time (s)")
fig.suptitle("skyforge: simple takeoff and climb")
plt.tight_layout()
plt.show()
