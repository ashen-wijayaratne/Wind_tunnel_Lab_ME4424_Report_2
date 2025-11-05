import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Your wake survey data from lecture notes
data = {
    'Distance from floor (m)': [0.1016, 0.127, 0.1524, 0.1778, 0.2032, 0.2286, 0.254, 0.2794, 0.3048, 0.3302, 
                               0.3556, 0.381, 0.4064, 0.4318, 0.4572, 0.4826, 0.508000001, 0.533400001, 
                               0.558800001, 0.584200001, 0.609600001, None],
    'Dynamic Pressure (Pa)': [76, 75, 74, 71, 65, 57, 51, 48, 46, 51, 55, 55, 64, 68, 76, 77, 75, 85, 86, 85, 85, 79],
    'Velocity (m/s)': [11.13919, 11.06567, 10.99165, 10.76654, 10.30158, 9.646825, 9.124983, 8.852533, 
                      8.666143, 9.124983, 9.476071, 9.476071, 10.22203, 10.53662, 11.13919, 11.21224, 
                      11.06567, 11.7803, 11.8494, 11.7803, 11.7803, 11.35692]
}

# Create DataFrame from data
df = pd.DataFrame(data)
df = df.dropna(subset=['Distance from floor (m)'])

# Sort by distance for proper plotting
df = df.sort_values('Distance from floor (m)')

# Print some key statistics first (so we see them immediately)
print("Wake Survey Statistics:")
print(f"Number of measurement points: {len(df)}")
print(f"Velocity range: {df['Velocity (m/s)'].min():.2f} - {df['Velocity (m/s)'].max():.2f} m/s")
print(f"Measurement height range: {df['Distance from floor (m)'].min():.3f} - {df['Distance from floor (m)'].max():.3f} m")
print()

# User-specified freestream velocity - using value from lecture notes
U_inf = 11.36  # [m/s]

# Now perform momentum integration for drag calculation
rho = 1.225  # [kg/m³] (air density at sea level)
b = 0.71      # [m]    (span)

# Calculate momentum deficit at each point
df['Momentum_Deficit'] = df['Velocity (m/s)'] * (U_inf - df['Velocity (m/s)'])

# Numerical integration using trapezoidal rule
drag_force = rho * b * np.trapezoid(df['Momentum_Deficit'], df['Distance from floor (m)'])

print("Momentum Equation Drag Calculation:")
print(f"Freestream velocity: {U_inf:.2f} m/s (user-specified)")
print(f"Drag force from momentum equation: {drag_force:.4f} N")

# Calculate drag coefficient
q = 0.5 * rho * U_inf**2
S = 0.12425  # reference area
C_d_momentum = drag_force / (q * S)
print(f"Drag coefficient from momentum: {C_d_momentum:.4f}")
print()

# Create the velocity profile plot
plt.figure(figsize=(10, 8))
plt.plot(df['Velocity (m/s)'], df['Distance from floor (m)'], 'bo-', linewidth=2, markersize=6, label='Wake Velocity Profile')
plt.xlabel('Velocity (m/s)', fontsize=12)
plt.ylabel('Distance from Floor (m)', fontsize=12)
plt.title('Wake Survey Velocity Profile\n(For Momentum Equation Drag Calculation)', fontsize=14)
plt.grid(True, alpha=0.3)

# Adding some annotations and *Aesthetics*
plt.axhline(y=df['Distance from floor (m)'].mean(), color='r', linestyle='--', alpha=0.7, 
           label=f"Mean Height: {df['Distance from floor (m)'].mean():.3f} m")
plt.axvline(x=U_inf, color='purple', linestyle='-', alpha=0.8, linewidth=2,
           label=f'Freestream Velocity: {U_inf:.2f} m/s')
plt.axvline(x=df['Velocity (m/s)'].max(), color='g', linestyle='--', alpha=0.7,
           label=f"Max Measured: {df['Velocity (m/s)'].max():.2f} m/s")

plt.legend()
plt.tight_layout()

plt.show(block=False) 
print("Plot displayed. Close the plot window to continue...")

# Keep the program running until plot is closed
plt.pause(0.001)
input("Press Enter to exit...")