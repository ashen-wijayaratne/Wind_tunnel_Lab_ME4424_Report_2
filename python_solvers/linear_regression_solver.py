import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('regression_plots', exist_ok=True)

# compact datasets definition
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

def regression_stats(Cl, Cm, angles, aoa_cut=16):
    """Compute regression statistics and sums for the linear region (α ≤ aoa_cut)."""
    mask = angles <= aoa_cut
    Cl_lin = Cl[mask]
    Cm_lin = Cm[mask]
    n = len(Cl_lin)

    sums = {
        'n': n,
        'sum_Cl': np.nan,
        'sum_Cm': np.nan,
        'sum_Cl_Cm': np.nan,
        'sum_Cl_sq': np.nan,
        'slope': np.nan,
        'intercept': np.nan,
        'h_ac': np.nan,
    }

    if n >= 2:
        sums['sum_Cl'] = Cl_lin.sum()
        sums['sum_Cm'] = Cm_lin.sum()
        sums['sum_Cl_Cm'] = (Cl_lin * Cm_lin).sum()
        sums['sum_Cl_sq'] = (Cl_lin**2).sum()
        denom = n * sums['sum_Cl_sq'] - sums['sum_Cl']**2
        if denom != 0:
            slope = (n * sums['sum_Cl_Cm'] - sums['sum_Cl'] * sums['sum_Cm']) / denom
            intercept = (sums['sum_Cm'] - slope * sums['sum_Cl']) / n
            sums.update({'slope': slope, 'intercept': intercept, 'h_ac': 0.25 - slope})

    return sums, mask


summary_rows = []
computation_rows = []
detail_rows = []
final_rows = []

for exp_name, data in datasets.items():
    Cl = data['Cl']
    Cm = data['Cm']
    angles = data['angles']

    stats, mask = regression_stats(Cl, Cm, angles)
    n = stats['n']

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(Cl, Cm, color='blue', label='All data points', zorder=5, s=50)
    if n > 0:
        plt.scatter(Cl[mask], Cm[mask], color='red', label='Linear region points (α ≤ 16°)', zorder=6, s=60)
    if not np.isnan(stats['slope']):
        Cl_line = np.linspace(Cl.min(), Cl.max(), 100)
        Cm_line = stats['slope'] * Cl_line + stats['intercept']
        plt.plot(Cl_line, Cm_line, color='red', linestyle='--', linewidth=2,
                 label=f'Regression line (slope = {stats["slope"]:.4f})')

    plt.xlabel('Lift Coefficient (C$_l$)', fontsize=12)
    plt.ylabel('Pitching Moment Coefficient (C$_m$)', fontsize=12)
    plt.title(f'Linear Regression of C$_m$ vs C$_l$\n{exp_name.replace("_", " ")}', fontsize=14)

    annotation_text = (
        f"Slope (dC$_m$/dC$_l$) = {stats['slope']:.4f}\n"
        f"Aerodynamic Center (h$_{{ac}}$/c) = {stats['h_ac']:.3f}\n"
        f"Points used: {n} (α ≤ 16°)"
    )
    plt.annotate(annotation_text, xy=(0.05, 0.95), xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8),
                 fontsize=10, verticalalignment='top')

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"regression_plots/{exp_name}_regression.png", dpi=300, bbox_inches='tight')
    plt.close()

    # collect rows for tables
    summary_rows.append({
        'Experiment': exp_name.replace('_', ' '),
        'Slope (dCm/dCl)': stats['slope'],
        'Intercept': stats['intercept'],
        'Aerodynamic Center (h_ac/c)': stats['h_ac'],
        'Points Used': n,
        'AoA Range': '−4° to 16°'
    })

    computation_rows.append({
        'Experiment': exp_name.replace('_', ' '),
        'n (Points)': n,
        '∑Cl': stats.get('sum_Cl', np.nan),
        '∑Cm': stats.get('sum_Cm', np.nan),
        '∑(Cl·Cm)': stats.get('sum_Cl_Cm', np.nan),
        '∑(Cl²)': stats.get('sum_Cl_sq', np.nan)
    })

    # detailed included/excluded points
    for idx in np.where(mask)[0]:
        detail_rows.append({'Experiment': exp_name.replace('_', ' '),
                            'Angle of Attack (°)': angles[idx],
                            'Cl (Included)': Cl[idx],
                            'Cm (Included)': Cm[idx]})
    for idx in np.where(~mask)[0]:
        detail_rows.append({'Experiment': exp_name.replace('_', ' '),
                            'Angle of Attack (°)': angles[idx],
                            'Cl (Excluded)': Cl[idx],
                            'Cm (Excluded)': Cm[idx]})

    if not np.isnan(stats['slope']):
        h_ac = stats['h_ac']
        final_rows.append({
            'Experiment': exp_name.replace('_', ' '),
            'dCm/dCl (Slope)': stats['slope'],
            'Cm0 (Intercept)': stats['intercept'],
            'h_ac/c': h_ac,
            'Distance from 0.25c': abs(h_ac - 0.25)
        })


print('\nAll plots have been saved to the "regression_plots" folder.\n')

print('\n' + '='*100)
print('REGRESSION RESULTS SUMMARY')
print('='*100)
print(pd.DataFrame(summary_rows).to_string(index=False, float_format=lambda x: f'{x:.6f}'))

print('\n' + '='*100)
print('DETAILED DATA POINTS (Included then Excluded)')
print('='*100)
if detail_rows:
    print(pd.DataFrame(detail_rows).to_string(index=False, float_format=lambda x: f'{x:.6f}'))
else:
    print('No detail rows to show.')

print('\n' + '='*100)
print('COMPUTATION TABLE: Sums for Linear Regression Calculations')
print('='*100)
print(pd.DataFrame(computation_rows).to_string(index=False, float_format=lambda x: f'{x:.6f}'))

print('\n' + '='*100)
print('KEY AERODYNAMIC PARAMETERS')
print('='*100)
print(pd.DataFrame(final_rows).to_string(index=False, float_format=lambda x: f'{x:.6f}'))
