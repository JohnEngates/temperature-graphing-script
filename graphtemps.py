#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Plot temperature, relative humidity, and dew point from an Excel file for a specified number of days.")
parser.add_argument("file_path", type=str, help="Path to the Excel file.")
parser.add_argument("-d", "--days", type=int, default=2, help="Number of days to graph (default: 2).")
args = parser.parse_args()

# Check if the file exists
if not os.path.exists(args.file_path):
    raise FileNotFoundError(f"The specified file does not exist: {args.file_path}")

# Load the data from the specified Excel file
df = pd.read_excel(args.file_path)

# Check for the correct column name and convert it to datetime format
if 'Date-Time (CDT)' in df.columns:
    datetime_column = 'Date-Time (CDT)'
elif 'Date-Time (CST/CDT)' in df.columns:
    datetime_column = 'Date-Time (CST/CDT)'
else:
    raise ValueError("No valid Date-Time column found.")

df[datetime_column] = pd.to_datetime(df[datetime_column])

# Set the datetime column as the index
df.set_index(datetime_column, inplace=True)

# Filter the data for the specified number of days
latest_date = df.index.max()  # Get the latest timestamp in the data
cutoff_date = latest_date - pd.Timedelta(days=args.days)  # Calculate the cutoff timestamp
df_filtered = df[df.index >= cutoff_date]  # Filter data for the specified number of days

# Plot Temperature, RH, and Dew Point over time
plt.figure(figsize=(14, 8))  # Set the figure size for the plots

# Plot Temperature
plt.subplot(3, 1, 1)  # Create the first subplot for Temperature
plt.plot(df_filtered.index, df_filtered['Temperature (°F) '], color='red')  # Plot temperature data
plt.title(f'Temperature Over Time (Last {args.days} Days)')  # Set the title for the temperature plot
plt.xlabel(datetime_column)  # Label the x-axis
plt.ylabel('Temperature (°F)')  # Label the y-axis
plt.grid(True)  # Add grid lines to the plot

# Plot Relative Humidity (RH)
plt.subplot(3, 1, 2)  # Create the second subplot for Relative Humidity
plt.plot(df_filtered.index, df_filtered['RH (%) '], color='blue')  # Plot relative humidity data
plt.title(f'Relative Humidity Over Time (Last {args.days} Days)')  # Set the title for the RH plot
plt.xlabel(datetime_column)  # Label the x-axis
plt.ylabel('RH (%)')  # Label the y-axis
plt.grid(True)  # Add grid lines to the plot

# Plot Dew Point
plt.subplot(3, 1, 3)  # Create the third subplot for Dew Point
plt.plot(df_filtered.index, df_filtered['Dew Point (°F) '], color='green')  # Plot dew point data
plt.title(f'Dew Point Over Time (Last {args.days} Days)')  # Set the title for the dew point plot
plt.xlabel(datetime_column)  # Label the x-axis
plt.ylabel('Dew Point (°F)')  # Label the y-axis
plt.grid(True)  # Add grid lines to the plot

# Adjust layout and show the plots
plt.tight_layout()  # Adjust the layout to prevent overlapping labels
plt.show()  # Display the plots

