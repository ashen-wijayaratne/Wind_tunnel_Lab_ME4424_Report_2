import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('regression_plots', exist_ok=True)

# Define all four datasets from lab calculations
datasets = {
    'Experiment_1_2D_airfoil_low_Re': {
        'Cl': np.array([0.219, 0.515, 0.816, 1.059, 1.230, 1.330, 1.306, 1.306, 1.298]),
        'Cm': np.array([-0.087320271, -0.087453789, -0.056285658, -0.083613917, -0.085173052, 
                       -0.088358206, -0.113314182, -0.119997384, -0.124163071]),
        'angles': np.array([-4, 0, 4, 8, 12, 16, 17, 18, 20])
    },
    'Experiment_2_2D_airfoil_high_Re': {
        'Cl': np.array([0.047, 0.338, 0.655, 0.905, 1.072, 1.157, 1.146, 1.097, 1.093]),
        'Cm': np.array([-0.076997843, -0.057471156, -0.054130599, -0.051839529, -0.064091257,
                       -0.075497476, -0.090844304, -0.095154435, -0.106791884]),
        'angles': np.array([-4, 0, 4, 8, 12, 16, 17, 18, 20])
    },
    'Experiment_3_3D_airfoil': {
        'Cl': np.array([0.017, 0.279, 0.550, 0.765, 0.942, 1.074, 1.062, 1.074, 1.077]),
        'Cm': np.array([-0.10091933, -0.076467428, -0.072400268, -0.073229073, -0.080903977,
                       -0.089227422, -0.112009902, -0.123527623, -0.133407249]),
        'angles': np.array([-4, 0, 4, 8, 12, 16, 17, 18, 20])
    },
    'Experiment_4_3D_airfoil_high_Re': {
        'Cl': np.array([-0.00506009, 0.291584419, 0.544479017, 0.771548338, 0.956943851,
                       1.083356161, 1.097075841, 1.095730431, 1.105413116]),
        'Cm': np.array([-0.070500135, -0.063649553, -0.054527757, -0.05722711, -0.075309479,
                       -0.079515418, -0.096344357, -0.106985619, -0.123512666]),
        'angles': np.array([-4, 0, 4, 8, 12, 16, 17, 18, 20])
    }
}

# Process each dataset
for exp_name, data in datasets.items():
    Cl = data['Cl']
    Cm = data['Cm']
    angles = data['angles']
    
    print(f"\n=== {exp_name} ===")
    
    # Select linear region (first 6 points: α = -4° to 16°). After 16 degrees, stall effects occur.
    linear_indices = angles <= 16
    Cl_linear = Cl[linear_indices]
    Cm_linear = Cm[linear_indices]
    
    n = len(Cl_linear)
    
    if n < 2:
        print(f"Not enough data points in linear region for {exp_name}")
        continue
    
    # Calculate the required sums for linear region
    sum_Cl = np.sum(Cl_linear)
    sum_Cm = np.sum(Cm_linear)
    sum_Cl_Cm = np.sum(Cl_linear * Cm_linear)
    sum_Cl_squared = np.sum(Cl_linear**2)
    
    # Calculate the slope (dCm/dCl)
    denominator = (n * sum_Cl_squared - sum_Cl**2)
    if denominator == 0:
        print(f"Error: Division by zero for {exp_name}")
        continue
    
    slope = (n * sum_Cl_Cm - sum_Cl * sum_Cm) / denominator
    intercept = (sum_Cm - slope * sum_Cl) / n
    
    # Calculate aerodynamic center
    h_ac = 0.25 - slope
    
    print(f"Slope (dCm/dCl): {slope:.6f}")
    print(f"Aerodynamic Center (h_ac/c): {h_ac:.4f}")
    print(f"Linear region points used: {n} (α = -4° to 16°)")
    print("Calculations completed successfully.")
    
    # Create plot
    plt.figure(figsize=(10, 6))
    
    # Plot all data points
    plt.scatter(Cl, Cm, color='blue', label='All data points', zorder=5, s=50)
    
    # Highlight linear region points (first 6 points)
    plt.scatter(Cl_linear, Cm_linear, color='red', label='Linear region points (α ≤ 16°)', zorder=6, s=60)
    
    # Plot regression line through the entire Cl range for visibility
    Cl_line = np.linspace(min(Cl), max(Cl), 100)
    Cm_line = slope * Cl_line + intercept
    plt.plot(Cl_line, Cm_line, color='red', linestyle='--', linewidth=2,
             label=f'Regression line (slope = {slope:.4f})')
    
    # Add labels and title
    plt.xlabel('Lift Coefficient (C$_l$)', fontsize=12)
    plt.ylabel('Pitching Moment Coefficient (C$_m$)', fontsize=12)
    plt.title(f'Linear Regression of C$_m$ vs C$_l$\n{exp_name.replace("_", " ")}', fontsize=14)
    
    # Add annotation with slope and aerodynamic center
    annotation_text = f'Slope (dC$_m$/dC$_l$) = {slope:.4f}\nAerodynamic Center (h$_{{ac}}$/c) = {h_ac:.3f}\nPoints used: {n} (α ≤ 16°)'
    plt.annotate(annotation_text, xy=(0.05, 0.95), xycoords='axes fraction',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8),
                fontsize=10, verticalalignment='top')
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Adjust layout and save
    plt.tight_layout()
    filename = f"regression_plots/{exp_name}_regression.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved as: {filename}")
    
    plt.close()

print(f"\nAll plots have been saved to the 'regression_plots' folder.")