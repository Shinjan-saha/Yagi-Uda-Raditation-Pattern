import numpy as np
import matplotlib.pyplot as plt


n = int(input("Enter the number of angle readings: "))


angles = []
powers = []

print("Enter angle (in degrees) and power received (in arbitrary units):")
for i in range(n):
    angle = float(input(f"Angle {i+1}: "))
    power = float(input(f"Power {i+1}: "))
    angles.append(angle)
    powers.append(power)


angles = np.radians(angles)


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles, powers, marker='o', color='b', linestyle='-', linewidth=2)


ax.set_title("Radiation Pattern of a Yagi-Uda 3-element Antenna")
ax.set_rlabel_position(-22.5)  


plt.show()
