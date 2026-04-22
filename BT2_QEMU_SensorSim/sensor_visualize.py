import matplotlib
matplotlib.use('Agg')  # Bat buoc cho QEMU headless
import matplotlib.pyplot as plt
from sensor_sim import SimUltrasonic, SimPotentiometer
from time import sleep

# Khoi tao cam bien
us = SimUltrasonic(echo=24, trigger=23, base_distance=50.0)
pot = SimPotentiometer(initial_value=0.4)  # span = 40cm
span = pot.value * 100  # Chuyen sang cm

# Thu thap 50 mau
distances = []
for i in range(50):
    d = us.distance
    distances.append(d)
    print(f"  Mau {i+1}/50: {d:.1f} cm")
    sleep(0.1)

print(f"\nThu thap xong {len(distances)} mau.")

# Ve do thi
fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(distances))

# Line plot khoang cach
ax.plot(x, distances, 'b-', linewidth=1.5, label='Khoang cach (cm)')

# Duong nguong span (do, net dut)
ax.axhline(y=span, color='r', linestyle='--', linewidth=2, label=f'Span = {span:.0f} cm')

# To vung Span (distance < span)
ax.fill_between(x, 0, [min(d, span) for d in distances],
                alpha=0.2, color='red', label='Vung Span!')

# Nhan truc + tieu de
ax.set_title('Ultrasonic Sensor Simulation - Span Detection')
ax.set_xlabel('Sample')
ax.set_ylabel('Distance (cm)')
ax.set_ylim(0, max(distances) + 10)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sensor_chart.png', dpi=150)
print('Saved: sensor_chart.png')
