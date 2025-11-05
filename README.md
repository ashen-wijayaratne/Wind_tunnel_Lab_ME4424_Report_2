# Aerodynamics Lab Data Analysis Tools

This repository contains a collection of Python scripts and data files used to analyze wind tunnel test data for a NACA airfoil study. The analysis includes comparisons of 2D and 3D airfoil performance, drag measurements, and stability characteristics calculations.

## Project Structure

```
├── python_solvers
│   ├── linear_regression_solver.py       # Performs linear regression analysis on airfoil data
│   ├── momentum_velocity_profile_solver.py # Calculates drag using momentum equation and wake profiles
│   ├── NACA_data_extractor.py           # Extracts data from NACA airfoil databases
│   └── NACA_matching.py                  # Matches experimental data with NACA airfoil profiles
├── supporting_CSVs
│   ├── input_velocity_profile.csv        # Velocity profile measurements
│   └── intial_LabData.csv               # Raw experimental measurements
├── Output Data
│   ├── regression_plots/                 # Generated regression analysis plots
│   └── xfoil_comprehensive_outputs/      # XFOIL analysis results and polar data - only a sample of the data included since output is large
```

## Features

- **Momentum Equation Analysis**: Calculates drag force using velocity wake profiles and the momentum equation
- **NACA Profile Matching**: Identifies the tested airfoil by comparing experimental data with XFOIL-generated NACA profiles
- **Aerodynamic Center Calculation**: Determines aerodynamic center location for different Reynolds numbers and configurations
- **Linear Regression Analysis**: Performs regression analysis on experimental data for various aerodynamic parameters

## Key Constants and Parameters

### Experimental Conditions

- Pressure: 102.7 Pa
- Temperature: 291.75 K
- Air Density: 1.227 kg/m³
- Viscosity: 1.807E-05 Ns/m²
- Speed of Sound: 342.38 m/s

### Wing Details

- NACA Code: 4412
- Chord Length: 0.175 m
- Span: 0.71 m
- Wing Area: 0.12425 m²
- Aspect Ratio (3D): 4.057
- Oswald Efficiency: 0.932

## Analysis Results

The code has successfully analyzed:

- Drag coefficients through direct and indirect measurements
- 2D vs 3D airfoil performance comparisons
- Aerodynamic center locations for different experimental configurations
- Reynolds number effects on aerodynamic characteristics

## Prerequisites

- Python 3.x
- Required Python packages (numpy, pandas, matplotlib)
- XFOIL data for NACA airfoils

## Usage

1. Place experimental data in CSV format in the project root directory
2. Run the appropriate Python scripts for specific analyses:
   ```
   python momentum_velocity_profile_solver.py  # For drag calculations
   python NACA_matching.py                    # For airfoil profile matching
   ```

## Data Processing Workflow

1. Raw data is read from `intial_LabData.csv`
2. Calculations and analysis are performed using various Python scripts
3. Results are stored in `Final_Report2_Data.csv`
4. Additional analysis outputs are saved in respective directories

## Notes

- All calculations use SI units
- Experimental data includes both 2D (with endplates) and 3D (without endplates) configurations
- Analysis accounts for strut tare drag and endplate effects
