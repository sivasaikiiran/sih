import pandas as pd
import numpy as np

# Function to calculate the purity percentage
def calculate_purity(sample_df, standard_df):
    # Ensure that both dataframes have the same length and matching wavenumbers
    if len(sample_df) != len(standard_df):
        raise ValueError("Sample and Standard files must have the same length")
    
    # Merge data on the wavenumber column (assuming both files have a 'Wavelength' column)
    merged_df =pd.merge(sample_df, standard_df, on='wavelength', suffixes=('_sample', '_standard'))

    # Calculate the absolute difference between sample and standard transmittance
    merged_df['Transmittance_Diff'] = np.abs(merged_df['%Transmitance_sample'] - merged_df['%Transmittance_standard'])
    
    # Calculate the average transmittance difference
    avg_diff = merged_df['Transmittance_Diff'].mean()
    
    # Calculate purity as a percentage
    purity_percentage = 100 - avg_diff  # Assuming 100% is perfect match
    
    return purity_percentage

# Function to read the CSV file and return a DataFrame
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Example usage
sample_file = 'sample.csv'    # Path to sample CSV file
standard_file = 'standard.csv'  # Path to standard CSV file

# Load the data from CSV files
sample_df = load_csv(sample_file)
standard_df = load_csv(standard_file)

# Calculate the purity percentage
purity = calculate_purity(sample_df, standard_df)
print(f"Purity Percentage: {purity:.2f}%")
