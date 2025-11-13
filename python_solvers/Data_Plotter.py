import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Read the CSV file
df = pd.read_csv('Rosie_Final_data.csv')

# Create main output folder
main_folder = "Ashens_plots"
os.makedirs(main_folder, exist_ok=True)

# Define colour scheme
colors = {
    'Experiment_1 2D airfoil at Low Re': 'skyblue',
    'Experiment_2 2D airfoil at High Re': 'lightgreen',
    'Experiment_3 3D airfoil at Low Re': 'purple',
    'Experiment_4 3D airfoil at High Re': 'red'
}

# Define short labels for legend
labels = {
    'Experiment_1 2D airfoil at Low Re': 'Exp 1: 2D Low Re',
    'Experiment_2 2D airfoil at High Re': 'Exp 2: 2D High Re',
    'Experiment_3 3D airfoil at Low Re': 'Exp 3: 3D Low Re',
    'Experiment_4 3D airfoil at High Re': 'Exp 4: 3D High Re'
}

# Separate experiments
exp_1 = df[df['Experiment'] == 'Experiment_1 2D airfoil at Low Re']
exp_2 = df[df['Experiment'] == 'Experiment_2 2D airfoil at High Re']
exp_3 = df[df['Experiment'] == 'Experiment_3 3D airfoil at Low Re']
exp_4 = df[df['Experiment'] == 'Experiment_4 3D airfoil at High Re']

experiments_2D = [exp_1, exp_2]
experiments_3D = [exp_3, exp_4]
all_experiments = [exp_1, exp_2, exp_3, exp_4]

# ============================================================================
# 1. Cd vs AoA Plots
# ============================================================================
folder_cd = os.path.join(main_folder, "Cd_vs_AoA")
os.makedirs(folder_cd, exist_ok=True)

# Plot 1: Both 2D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_2D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['C_d  [realDrag/q*S]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Coefficient of Drag, $C_d$', fontsize=12)
plt.title('Drag Coefficient vs Angle of Attack - 2D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cd, '1_Cd_vs_AoA_2D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Both 3D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_3D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['C_d  [realDrag/q*S]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Coefficient of Drag, $C_d$', fontsize=12)
plt.title('Drag Coefficient vs Angle of Attack - 3D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cd, '2_Cd_vs_AoA_3D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: All experiments
plt.figure(figsize=(10, 6))
for exp in all_experiments:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['C_d  [realDrag/q*S]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)

# Print summary table of graph data
print("\n" + "="*80)
print("Cd vs AoA - All Experiments")
print("="*80)
aoa = exp_1['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 1: 2D Low Re': exp_1['C_d  [realDrag/q*S]'].values,
    'Exp 2: 2D High Re': exp_2['C_d  [realDrag/q*S]'].values,
    'Exp 3: 3D Low Re': exp_3['C_d  [realDrag/q*S]'].values,
    'Exp 4: 3D High Re': exp_4['C_d  [realDrag/q*S]'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.4f}'))
print("="*80 + "\n")

plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Coefficient of Drag, $C_d$', fontsize=12)
plt.title('Drag Coefficient vs Angle of Attack - All Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cd, '3_Cd_vs_AoA_All.png'), dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 2. Lift (N) vs AoA Plots
# ============================================================================
folder_lift = os.path.join(main_folder, "Lift_vs_AoA")
os.makedirs(folder_lift, exist_ok=True)

# Plot 1: Both 2D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_2D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Lift (N) [lab data]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Lift (N)', fontsize=12)
plt.title('Lift vs Angle of Attack - 2D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0) 
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_lift, '1_Lift_vs_AoA_2D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Both 3D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_3D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Lift (N) [lab data]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Lift (N)', fontsize=12)
plt.title('Lift vs Angle of Attack - 3D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_lift, '2_Lift_vs_AoA_3D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: All experiments
plt.figure(figsize=(10, 6))
for exp in all_experiments:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Lift (N) [lab data]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)

# Print consolidated table
print("\n" + "="*80)
print("Lift vs AoA - All Experiments")
print("="*80)
aoa = exp_1['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 1: 2D Low Re': exp_1['Lift (N) [lab data]'].values,
    'Exp 2: 2D High Re': exp_2['Lift (N) [lab data]'].values,
    'Exp 3: 3D Low Re': exp_3['Lift (N) [lab data]'].values,
    'Exp 4: 3D High Re': exp_4['Lift (N) [lab data]'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.4f}'))
print("="*80 + "\n")

plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Lift (N)', fontsize=12)
plt.title('Lift vs Angle of Attack - All Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_lift, '3_Lift_vs_AoA_All.png'), dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. Cl vs AoA Plots
# ============================================================================
folder_cl = os.path.join(main_folder, "Cl_vs_AoA")
os.makedirs(folder_cl, exist_ok=True)

# Plot 1: Both 2D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_2D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Cl [L/(q·S)]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Coefficient of Lift, $C_l$', fontsize=12)
plt.title('Lift Coefficient vs Angle of Attack - 2D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cl, '1_Cl_vs_AoA_2D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Both 3D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_3D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Cl [L/(q·S)]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Coefficient of Lift, $C_l$', fontsize=12)
plt.title('Lift Coefficient vs Angle of Attack - 3D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cl, '2_Cl_vs_AoA_3D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: All experiments
plt.figure(figsize=(10, 6))
for exp in all_experiments:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Cl [L/(q·S)]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)

# Print consolidated table
print("\n" + "="*80)
print("Cl vs AoA - All Experiments")
print("="*80)
aoa = exp_1['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 1: 2D Low Re': exp_1['Cl [L/(q·S)]'].values,
    'Exp 2: 2D High Re': exp_2['Cl [L/(q·S)]'].values,
    'Exp 3: 3D Low Re': exp_3['Cl [L/(q·S)]'].values,
    'Exp 4: 3D High Re': exp_4['Cl [L/(q·S)]'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.4f}'))
print("="*80 + "\n")

plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Coefficient of Lift, $C_l$', fontsize=12)
plt.title('Lift Coefficient vs Angle of Attack - All Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cl, '3_Cl_vs_AoA_All.png'), dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 4. Cm vs AoA Plots
# ============================================================================
folder_cm = os.path.join(main_folder, "Cm_vs_AoA")
os.makedirs(folder_cm, exist_ok=True)

# Plot 1: Both 2D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_2D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Cm [M/(q·S·c)]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Pitching Moment Coefficient, $C_m$', fontsize=12)
plt.title('Pitching Moment Coefficient vs Angle of Attack - 2D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cm, '1_Cm_vs_AoA_2D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Both 3D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_3D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Cm [M/(q·S·c)]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Pitching Moment Coefficient, $C_m$', fontsize=12)
plt.title('Pitching Moment Coefficient vs Angle of Attack - 3D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cm, '2_Cm_vs_AoA_3D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: All experiments
plt.figure(figsize=(10, 6))
for exp in all_experiments:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['Cm [M/(q·S·c)]'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)

# Print consolidated table
print("\n" + "="*80)
print("Cm vs AoA - All Experiments")
print("="*80)
aoa = exp_1['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 1: 2D Low Re': exp_1['Cm [M/(q·S·c)]'].values,
    'Exp 2: 2D High Re': exp_2['Cm [M/(q·S·c)]'].values,
    'Exp 3: 3D Low Re': exp_3['Cm [M/(q·S·c)]'].values,
    'Exp 4: 3D High Re': exp_4['Cm [M/(q·S·c)]'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.4f}'))
print("="*80 + "\n")

plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Pitching Moment Coefficient, $C_m$', fontsize=12)
plt.title('Pitching Moment Coefficient vs Angle of Attack - All Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_cm, '3_Cm_vs_AoA_All.png'), dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 5. L/D Ratio vs AoA Plots
# ============================================================================
folder_ld = os.path.join(main_folder, "LD_ratio_vs_AoA")
os.makedirs(folder_ld, exist_ok=True)

# Calculate L/D ratio
df['L/D'] = df['Lift (N) [lab data]'] / df['Real Airfoil Drag [Nominal Drag - Parasitic Drag]']

# Update experiment dataframes with L/D
exp_1 = df[df['Experiment'] == 'Experiment_1 2D airfoil at Low Re']
exp_2 = df[df['Experiment'] == 'Experiment_2 2D airfoil at High Re']
exp_3 = df[df['Experiment'] == 'Experiment_3 3D airfoil at Low Re']
exp_4 = df[df['Experiment'] == 'Experiment_4 3D airfoil at High Re']

experiments_2D = [exp_1, exp_2]
experiments_3D = [exp_3, exp_4]
all_experiments = [exp_1, exp_2, exp_3, exp_4]

# Plot 1: Both 2D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_2D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['L/D'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Lift-to-Drag Ratio, L/D', fontsize=12)
plt.title('Lift-to-Drag Ratio vs Angle of Attack - 2D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_ld, '1_LD_vs_AoA_2D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Both 3D experiments
plt.figure(figsize=(10, 6))
for exp in experiments_3D:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['L/D'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)
plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Lift-to-Drag Ratio, L/D', fontsize=12)
plt.title('Lift-to-Drag Ratio vs Angle of Attack - 3D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_ld, '2_LD_vs_AoA_3D.png'), dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: All experiments
plt.figure(figsize=(10, 6))
for exp in all_experiments:
    exp_name = exp['Experiment'].iloc[0]
    plt.plot(exp['AoA (°) [lab data]'], exp['L/D'], 
             marker='o', color=colors[exp_name], label=labels[exp_name], linewidth=2)

# Print consolidated table
print("\n" + "="*80)
print("L/D Ratio vs AoA - All Experiments")
print("="*80)
aoa = exp_1['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 1: 2D Low Re': exp_1['L/D'].values,
    'Exp 2: 2D High Re': exp_2['L/D'].values,
    'Exp 3: 3D Low Re': exp_3['L/D'].values,
    'Exp 4: 3D High Re': exp_4['L/D'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.2f}'))
print("="*80 + "\n")

plt.xlabel('Angle of Attack (°)', fontsize=12)
plt.ylabel('Lift-to-Drag Ratio, L/D', fontsize=12)
plt.title('Lift-to-Drag Ratio vs Angle of Attack - All Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=1.0)
plt.xlim(left=min(df['AoA (°) [lab data]']) - 1, right=max(df['AoA (°) [lab data]']) + 2)
plt.ylim(bottom=0)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig(os.path.join(folder_ld, '3_LD_vs_AoA_All.png'), dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 6. Stacked Column Charts for Drag Components
# ============================================================================
folder_drag_comp = os.path.join(main_folder, "Drag_components")
os.makedirs(folder_drag_comp, exist_ok=True)

# Plotting 2D experiments together on same chart
plt.figure(figsize=(14, 7))
aoa = exp_1['AoA (°) [lab data]'].values
x_pos = np.arange(len(aoa))
bar_width = 0.35
group_spacing = bar_width + 0.05

# Exp 1 & 2 data
exp1_sf = exp_1['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values
exp1_pd = exp_1['Wing Pressure drag [q*S*CD]'].values
exp2_sf = exp_2['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values
exp2_pd = exp_2['Wing Pressure drag [q*S*CD]'].values

# Create grouped stacked bars
p1 = plt.bar(x_pos - bar_width/2 - 0.025, exp1_sf, bar_width, label='Exp 1: Skin Friction', color='#3498db', alpha=0.9)
p2 = plt.bar(x_pos - bar_width/2 - 0.025, exp1_pd, bar_width, bottom=exp1_sf, label='Exp 1: Pressure Drag', color='#e74c3c', alpha=0.9)

p3 = plt.bar(x_pos + bar_width/2 + 0.025, exp2_sf, bar_width, label='Exp 2: Skin Friction', color='#3498db', alpha=0.6)
p4 = plt.bar(x_pos + bar_width/2 + 0.025, exp2_pd, bar_width, bottom=exp2_sf, label='Exp 2: Pressure Drag', color='#e74c3c', alpha=0.6)

plt.xticks(x_pos, [f'{int(a)}°' for a in aoa], fontsize=10)
plt.xlabel('Angle of Attack', fontsize=12)
plt.ylabel('Drag Components', fontsize=12)
plt.title('Drag Components vs Angle of Attack - 2D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=9, loc='upper left', ncol=2)
plt.grid(True, alpha=0.3, axis='y')
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig(os.path.join(folder_drag_comp, '1_Drag_Components_2D_Combined.png'), 
            dpi=300, bbox_inches='tight')
plt.close()

# Plot 3D experiments together on same chart (grouped stacked bars)
plt.figure(figsize=(14, 7))
aoa = exp_3['AoA (°) [lab data]'].values
x_pos = np.arange(len(aoa))
bar_width = 0.35

# Exp 3 data (3D Low Re)
exp3_sf = exp_3['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values
exp3_pd = exp_3['Wing Pressure drag [q*S*CD]'].values
exp3_id = exp_3['CD induced [(Cl^2) / (π * e * AR)]'].values

# Exp 4 data (3D High Re)
exp4_sf = exp_4['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values
exp4_pd = exp_4['Wing Pressure drag [q*S*CD]'].values
exp4_id = exp_4['CD induced [(Cl^2) / (π * e * AR)]'].values

# Create grouped stacked bars (3 components for each experiment)
p1 = plt.bar(x_pos - bar_width/2 - 0.025, exp3_sf, bar_width, label='Exp 3: Skin Friction', color='#3498db', alpha=0.9)
p2 = plt.bar(x_pos - bar_width/2 - 0.025, exp3_pd, bar_width, bottom=exp3_sf, label='Exp 3: Pressure Drag', color='#e74c3c', alpha=0.9)
p3 = plt.bar(x_pos - bar_width/2 - 0.025, exp3_id, bar_width, bottom=exp3_sf + exp3_pd, label='Exp 3: Induced Drag', color='#f39c12', alpha=0.9)

p4 = plt.bar(x_pos + bar_width/2 + 0.025, exp4_sf, bar_width, label='Exp 4: Skin Friction', color='#3498db', alpha=0.6)
p5 = plt.bar(x_pos + bar_width/2 + 0.025, exp4_pd, bar_width, bottom=exp4_sf, label='Exp 4: Pressure Drag', color='#e74c3c', alpha=0.6)
p6 = plt.bar(x_pos + bar_width/2 + 0.025, exp4_id, bar_width, bottom=exp4_sf + exp4_pd, label='Exp 4: Induced Drag', color='#f39c12', alpha=0.6)

plt.xticks(x_pos, [f'{int(a)}°' for a in aoa], fontsize=10)
plt.xlabel('Angle of Attack', fontsize=12)
plt.ylabel('Drag Components', fontsize=12)
plt.title('Drag Components vs Angle of Attack - 3D Experiments', fontsize=14, fontweight='bold')
plt.legend(fontsize=8, loc='upper left', ncol=3)
plt.grid(True, alpha=0.3, axis='y')
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig(os.path.join(folder_drag_comp, '2_Drag_Components_3D_Combined.png'), 
            dpi=300, bbox_inches='tight')
plt.close()

# Print consolidated tables for 2D experiments
print("\n" + "="*80)
print("Drag Components - 2D Experiments")
print("="*80)
aoa = exp_1['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 1 Skin Friction': exp_1['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values,
    'Exp 1 Pressure Drag': exp_1['Wing Pressure drag [q*S*CD]'].values,
    'Exp 2 Skin Friction': exp_2['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values,
    'Exp 2 Pressure Drag': exp_2['Wing Pressure drag [q*S*CD]'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.2f}'))
print("="*80 + "\n")

# Print consolidated tables for 3D experiments
print("\n" + "="*80)
print("Drag Components - 3D Experiments")
print("="*80)
aoa = exp_3['AoA (°) [lab data]'].values
table_data = {
    'AoA (°)': aoa,
    'Exp 3 Skin Friction': exp_3['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values,
    'Exp 3 Pressure Drag': exp_3['Wing Pressure drag [q*S*CD]'].values,
    'Exp 3 Induced Drag': exp_3['CD induced [(Cl^2) / (π * e * AR)]'].values,
    'Exp 4 Skin Friction': exp_4['Wing Skin Friction [q*S*2*(0.074/(RE)^0.2)]'].values,
    'Exp 4 Pressure Drag': exp_4['Wing Pressure drag [q*S*CD]'].values,
    'Exp 4 Induced Drag': exp_4['CD induced [(Cl^2) / (π * e * AR)]'].values,
}
df_table = pd.DataFrame(table_data)
print(df_table.to_string(index=False, float_format=lambda x: f'{x:.2f}'))
print("="*80 + "\n")

print("\n" + "="*80)
print("All plots have been generated successfully!")
print(f"Plots saved in '{main_folder}' directory")
print("Happy plotting!")
print("\n" + "="*80)
print()
