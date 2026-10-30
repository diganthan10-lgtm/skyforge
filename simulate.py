import numpy as np
import matplotlib.pyplot as plt

from aircraft import mass, wing_area, thrust, cd0, k, cl_max, rho as rho0, g
dt = 0.1
t_end = 120.0
steps = int(t_end / dt)

# State: x (distance), h (altitude), v (airspeed), gamma (flight path angle)
x, h, v, gamma = 0.0, 0.0, 0.0, 0.0

time, altitude, speed, aoa = [], [], [], []

for i in range(steps):
    rho = rho0 * np.exp(-h / 8500)  # simple exponential atmosphere
    q = 0.5 * rho * v**2

    cl = (mass * g * np.cos(gamma)) / (q * wing_area) if q > 0 else 0.0
    cl = min(cl, cl_max)
    cd = cd0 + k * cl**2
    drag = q * wing_area * cd
    lift = q * wing_area * cl

    # Accelerations along and perpendicular to the flight path
    dv = (thrust - drag - mass * g * np.sin(gamma)) / mass
    dgamma = (lift - mass * g * np.cos(gamma)) / (mass * max(v, 1.0))

    v = max(v + dv * dt, 0.0)
    gamma = gamma + dgamma * dt
    x += v * np.cos(gamma) * dt
    h += v * np.sin(gamma) * dt
    h = max(h, 0.0)

    time.append(i * dt)
    altitude.append(h)
    speed.append(v)
    aoa.append(np.degrees(gamma))

fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
axes[0].plot(time, altitude); axes[0].set_ylabel("Altitude (m)")
axes[1].plot(time, speed);    axes[1].set_ylabel("Airspeed (m/s)")
axes[2].plot(time, aoa);      axes[2].set_ylabel("Flight path angle (deg)")
axes[2].set_xlabel("Time (s)")
fig.suptitle("skyforge: simple takeoff and climb")
plt.tight_layout()
plt.show()
