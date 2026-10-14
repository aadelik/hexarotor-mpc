import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

L1_XY = 1.35 * 0.3048
L2_XY = 0.51

# 1. Lateral Path (XY)
plt.figure(figsize=(10, 6))
plt.plot(df['ref_x'], df['ref_y'], 'k--', linewidth=1.5, label='Reference')
plt.plot(df['ref_x'], df['ref_y'] + L1_XY, 'g:', linewidth=1.5, label='Level 1 Limit')
plt.plot(df['ref_x'], df['ref_y'] - L1_XY, 'g:', linewidth=1.5)
plt.plot(df['ref_x'], df['ref_y'] + L2_XY, color='gray', linestyle='--', linewidth=1.0, label='Level 2 Limit')
plt.plot(df['ref_x'], df['ref_y'] - L2_XY, color='gray', linestyle='--', linewidth=1.0)
plt.plot(df['x'], df['y'], 'b-', linewidth=2.0, label='Trajectory')

plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Lateral Path (XY)')
plt.grid(True)
plt.legend(loc='upper right')
plt.xlim(min(df['ref_x']), max(df['ref_x']))
plt.savefig('plot_XY.png', dpi=300)
plt.savefig('plot_XY.pdf', dpi=300)

# 2. ACM & Wind Overlay
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:green'
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Available Control Margin (h)', color='black')
ax1.plot(df['time'], df['h'], color=color, linewidth=2.0, linestyle='--', label='With RG')
ax1.axhline(1.0, color='red', linestyle='-', linewidth=1.5, label='Level 1 Limit (h=1.0)')
ax1.axhline(0.0, color='blue', linestyle='-', linewidth=1.5, label='Level 3 Limit (h=0.0)')
ax1.set_ylim(-0.2, 1.5)
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True)

ax2 = ax1.twinx()  
color2 = 'tab:orange'
ax2.set_ylabel('Wind Vel [m/s]', color=color2)  
ax2.plot(df['time'], df['wind_vel'], color=color2, linewidth=1.5, label='Wind Velocity')
ax2.set_ylim(0, 12)
ax2.tick_params(axis='y', labelcolor=color2)

fig.tight_layout() 
plt.title('Actuator Health & Disturbance')
plt.savefig('plot_ACM.png', dpi=300)
plt.savefig('plot_ACM.pdf', dpi=300)