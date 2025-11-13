# Aerodynamics Lab Data Analysis Tools

This repository contains a comprehensive suite of Python scripts designed for analyzing wind tunnel test data of NACA airfoils. The toolset enables detailed analysis of aerodynamic characteristics, including lift and drag measurements, stability parameters, and performance comparisons between 2D and 3D configurations.

## Project Structure

```
├── python_solvers/
│   ├── linear_regression_solver.py       # Linear regression analysis for aerodynamic coefficients
│   ├── momentum_velocity_profile_solver.py # Wake analysis and momentum-based drag calculations
│   ├── NACA_data_extractor.py           # XFOIL data parser for NACA airfoil databases
│   └── NACA_matching.py                  # Automated NACA airfoil profile identification
│   └── Data_Plotter.py              # Automated plot generation
├── supporting_CSVs/
│   ├── input_velocity_profile.csv        # Velocity wake profile measurements
│   └── intial_LabData.csv               # Raw wind tunnel experimental data
├── Output Data/
│   ├── regression_plots/                 # Generated analysis visualizations
│   └── xfoil_comprehensive_outputs/      # Sample XFOIL analysis results (subset of full data)
```

## Detailed Component Description

### Python Solvers

#### linear_regression_solver.py

- Performs advanced regression analysis on aerodynamic data
- Determines aerodynamic centre locations through moment coefficient analysis
- Prints out tabulated summaries

#### momentum_velocity_profile_solver.py

- Implements the momentum integral equation for drag calculation
- Processes wake velocity profiles using trapezoidal numerical integration

#### NACA_data_extractor.py

- Interfaces with XFOIL to generate theoretical airfoil data
- Extracts performance polars for various Reynolds numbers
- Processes and formats XFOIL output for comparison with experimental data
- Handles batch processing of multiple NACA profiles

#### NACA_matching.py

- Implements the Root Mean Square Error method for matching algorithms to identify unknown airfoil profiles.
- Compares experimental data against a comprehensive NACA database

#### Data_PLotter.py

- This script generates various plots for drag, lift, and moment coefficients against angle of attack from experimental data. It includes functions for plotting 2D and 3D experiments, saving the plots, and printing summary tables.

### Data Files

- **input_velocity_profile.csv**: Contains detailed wake velocity measurements at various angles of attack
- **intial_LabData.csv**: Raw experimental measurements, including:
  - Force balance readings (lift, drag, moment)
  - Flow conditions (velocity, pressure, temperature)
  - Geometric parameters (angle of attack, configuration details)


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

## Prerequisites

- Python 3.x
- Required Python packages (numpy, pandas, matplotlib)
- XFOIL data for NACA airfoils

## Usage Guide

### Setup and Dependencies

```bash
pip install numpy pandas matplotlib scipy
```

### Analysis Workflow

1. **Data Preparation**

   - Place your wind tunnel test data in CSV format in `supporting_CSVs/`
   - Ensure data follows the format specified in `intial_LabData.csv`
   - Wake profile measurements should match `input_velocity_profile.csv` structure

2. **Running Analysis Scripts**

   For wake analysis and drag calculations:

   ```bash
   python python_solvers/momentum_velocity_profile_solver.py
   ```

   For NACA airfoil identification:

   ```bash
   python python_solvers/NACA_matching.py
   ```

   For aerodynamic coefficient analysis:

   ```bash
   python python_solvers/linear_regression_solver.py
   ```

3. **Output Processing**
   - Regression plots are automatically generated in `regression_plots/`
   - XFOIL comparison data is saved in `xfoil_comprehensive_outputs/`
   - Analysis results can be found in generated CSV files

### Advanced Usage

- Modify Reynolds number ranges in script parameters for different flow conditions
- Adjust integration parameters in momentum solver for different wake profiles
- Configure regression analysis parameters for different confidence levels
- Customize NACA profile search range for airfoil matching

## Notes

- All calculations use SI units
- Experimental data includes both 2D (with endplates) and 3D (without endplates) configurations
- Analysis accounts for strut tare drag and endplate effects
