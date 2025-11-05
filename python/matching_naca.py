#!/usr/bin/env python3
"""
Reduced NACA Airfoil Matcher
Keeps only combined RMSE (CL+CM) and CL-only RMSE rankings.
Excludes 20° angle due to stall effects.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Experimental data - EXCLUDING 20° due to XFOIL returning unreliable data during stall effects
EXPERIMENTAL_DATA = {
    'Alpha': [-4.0, 0.0, 4.0, 8.0, 12.0, 16.0],
    'CL': [0.219, 0.515, 0.816, 1.059, 1.23, 1.33],
    'CM': [-0.08732, -0.08745, -0.05629, -0.08361, -0.08517, -0.08836],
}

def interp_values_for_alphas(exp_alphas, sim_df, columns):
    """Return list(s) of interpolated simulation values for each column at exp_alphas."""
    results = {col: [] for col in columns}

    for alpha in exp_alphas:
        match = sim_df[sim_df['Alpha'] == alpha]
        if len(match) > 0:
            for col in columns:
                results[col].append(match.iloc[0][col])
        else:
            closest = sim_df.iloc[(sim_df['Alpha'] - alpha).abs().argsort()[:2]]
            if len(closest) == 2:
                x1, x2 = closest['Alpha'].values
                for col in columns:
                    y1, y2 = closest[col].values
                    interp = y1 + (y2 - y1) * (alpha - x1) / (x2 - x1)
                    results[col].append(interp)
            else:
                # cannot interpolate reliably
                return None
    return results

# Function to calculate RMSEs
def calculate_combined_rmse(exp_data, sim_data):
    """Return rmse_cl, rmse_cm and combined_rmse for a single airfoil simulation DataFrame."""
    aligned = interp_values_for_alphas(exp_data['Alpha'], sim_data, ['CL', 'CM'])
    if aligned is None:
        return None

    exp_cl = np.array(exp_data['CL'])
    exp_cm = np.array(exp_data['CM'])
    sim_cl = np.array(aligned['CL'])
    sim_cm = np.array(aligned['CM'])

    rmse_cl = np.sqrt(np.mean((exp_cl - sim_cl) ** 2))
    rmse_cm = np.sqrt(np.mean((exp_cm - sim_cm) ** 2))
    combined_rmse = 0.6 * rmse_cl + 0.4 * rmse_cm

    return {'rmse_cl': rmse_cl, 'rmse_cm': rmse_cm, 'combined_rmse': combined_rmse}

# Function to calculate CL-only RMSE
def calculate_cl_rmse(exp_data, sim_data):
    """Return rmse_cl only for a single airfoil simulation DataFrame."""
    aligned = interp_values_for_alphas(exp_data['Alpha'], sim_data, ['CL'])
    if aligned is None:
        return None

    exp_cl = np.array(exp_data['CL'])
    sim_cl = np.array(aligned['CL'])
    rmse_cl = np.sqrt(np.mean((exp_cl - sim_cl) ** 2))
    return {'rmse_cl': rmse_cl}

# Main function - reads the CSV, processes airfoils and then calculates RMSEs from above functions for all airfoils
def main():
    SIMULATION_CSV = Path("xfoil_comprehensive_outputs/airfoil_data.csv")

    if not SIMULATION_CSV.exists():
        print("Error: Run the data gathering script first!")
        sys.exit(1)

    sim_df = pd.read_csv(SIMULATION_CSV)
    airfoils = sim_df['Airfoil'].unique()

    print("Evaluating airfoils (combined RMSE and CL-only RMSE)...")
    print(f"Using angles: {EXPERIMENTAL_DATA['Alpha']} (20° excluded due to stall effects)")

    combined_results = []
    cl_only_results = []

    # Calculate both RMSE calculations for each airfoil
    for airfoil in airfoils:
        airfoil_data = sim_df[sim_df['Airfoil'] == airfoil].reset_index(drop=True)

        combined = calculate_combined_rmse(EXPERIMENTAL_DATA, airfoil_data)
        if combined is not None:
            row = {'Airfoil': airfoil}
            row.update(combined)
            combined_results.append(row)

        cl_only = calculate_cl_rmse(EXPERIMENTAL_DATA, airfoil_data)
        if cl_only is not None:
            row = {'Airfoil': airfoil}
            row.update(cl_only)
            cl_only_results.append(row)

    combined_df = pd.DataFrame(combined_results)
    cl_only_df = pd.DataFrame(cl_only_results)

    #OUTPUT: COMBINED RMSE (CL + CM)
    print("\n")
    print("COMBINED ANALYSIS (CL + CM) - TOP MATCHES BY COMBINED RMSE")
    if not combined_df.empty:
        rmse_rank = combined_df.nsmallest(10, 'combined_rmse')[['Airfoil', 'combined_rmse', 'rmse_cl', 'rmse_cm']]
        print(rmse_rank.to_string(index=False))
    else:
        print("No combined results available.")

    #OUTPUT: CL-ONLY RMSE
    print("\n")
    print("CL-ONLY ANALYSIS")
    if not cl_only_df.empty:
        cl_rmse_rank = cl_only_df.nsmallest(10, 'rmse_cl')[['Airfoil', 'rmse_cl']]
        print("\nTOP MATCHES BY CL RMSE")
        print("-" * 30)
        print(cl_rmse_rank.to_string(index=False))
    else:
        print("No CL-only results available.")

if __name__ == "__main__":
    main()
