# Data Analysis Guide

This page explains how to analyze and extract insights from the collected sensor data.

## Overview

Once you've collected sensor data through the River Project, you can perform various analyses to understand environmental patterns and trends.

## Setting Up Analysis Environment

### Required Libraries

```bash
pip install pandas numpy matplotlib scipy scikit-learn
```

### Import Statements

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime, timedelta
```

## Data Loading

### From CSV Files

```python
# Load sensor data from CSV
df = pd.read_csv('sensor_data.csv', parse_dates=['timestamp'])

# Display basic info
print(df.head())
print(df.info())
print(df.describe())
```

### From MQTT Database

```python
# Connect to database storing MQTT data
import sqlite3

conn = sqlite3.connect('sensor_data.db')
df = pd.read_sql_query("SELECT * FROM readings WHERE timestamp > ?", 
                       conn, 
                       params=(datetime.now() - timedelta(days=7),),
                       parse_dates=['timestamp'])
```

## Descriptive Statistics

### Basic Statistics

```python
# Calculate summary statistics
print(f"Temperature Mean: {df['temperature'].mean():.2f}°C")
print(f"Temperature Std Dev: {df['temperature'].std():.2f}°C")
print(f"Temperature Min: {df['temperature'].min():.2f}°C")
print(f"Temperature Max: {df['temperature'].max():.2f}°C")

# Humidity statistics
print(df['humidity'].describe())

# Correlation analysis
print(df.corr())
```

### Time-Based Analysis

```python
# Set timestamp as index
df.set_index('timestamp', inplace=True)

# Hourly averages
hourly_avg = df.resample('H').mean()

# Daily statistics
daily_stats = df.resample('D').agg({
    'temperature': ['mean', 'min', 'max'],
    'humidity': ['mean', 'min', 'max'],
    'pressure': 'mean'
})

print(daily_stats)
```

## Data Visualization

### Temperature Trends

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df['temperature'], label='Temperature', linewidth=2)
ax.set_xlabel('Time')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Temperature Over Time')
ax.legend()
ax.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Multiple Sensors

```python
fig, axes = plt.subplots(3, 1, figsize=(12, 10))

# Temperature
axes[0].plot(df.index, df['temperature'], color='red', label='Temperature')
axes[0].set_ylabel('Temperature (°C)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(df.index, df['humidity'], color='blue', label='Humidity')
axes[1].set_ylabel('Humidity (%)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(df.index, df['pressure'], color='green', label='Pressure')
axes[2].set_ylabel('Pressure (hPa)')
axes[2].set_xlabel('Time')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Distribution Analysis

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Temperature distribution
axes[0].hist(df['temperature'], bins=30, color='red', edgecolor='black')
axes[0].set_xlabel('Temperature (°C)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Temperature Distribution')

# Humidity distribution
axes[1].hist(df['humidity'], bins=30, color='blue', edgecolor='black')
axes[1].set_xlabel('Humidity (%)')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Humidity Distribution')

# Pressure distribution
axes[2].hist(df['pressure'], bins=30, color='green', edgecolor='black')
axes[2].set_xlabel('Pressure (hPa)')
axes[2].set_ylabel('Frequency')
axes[2].set_title('Pressure Distribution')

plt.tight_layout()
plt.show()
```

### Correlation Matrix

```python
import seaborn as sns

# Calculate correlation
corr_matrix = df[['temperature', 'humidity', 'pressure']].corr()

# Visualize
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Sensor Data Correlation Matrix')
plt.show()
```

## Statistical Analysis

### Trend Detection

```python
# Linear regression for trend
from scipy.stats import linregress

# Prepare data
x = np.arange(len(df))
y = df['temperature'].values

# Calculate trend
slope, intercept, r_value, p_value, std_err = linregress(x, y)

print(f"Trend slope: {slope:.6f}°C per reading")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value: {p_value:.4f}")

# Plot trend line
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['temperature'], label='Actual', linewidth=2)
plt.plot(df.index, slope * x + intercept, 'r--', label='Trend', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Anomaly Detection

```python
# Identify outliers using Z-score
from scipy.stats import zscore

df['temp_zscore'] = np.abs(zscore(df['temperature']))
anomalies = df[df['temp_zscore'] > 3]

print(f"Found {len(anomalies)} temperature anomalies")
print(anomalies)
```

### Seasonal Decomposition

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Perform decomposition
decomposition = seasonal_decompose(df['temperature'], model='additive', period=24)

# Plot components
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
decomposition.observed.plot(ax=axes[0], title='Observed')
decomposition.trend.plot(ax=axes[1], title='Trend')
decomposition.seasonal.plot(ax=axes[2], title='Seasonal')
decomposition.resid.plot(ax=axes[3], title='Residual')
plt.tight_layout()
plt.show()
```

## Environmental Pattern Analysis

### Diurnal Patterns

```python
# Extract hour from timestamp
df['hour'] = df.index.hour

# Calculate hourly averages
hourly_pattern = df.groupby('hour')[['temperature', 'humidity']].mean()

# Plot diurnal cycle
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hourly_pattern.index, hourly_pattern['temperature'], 
        marker='o', linewidth=2, label='Temperature')
ax.set_xlabel('Hour of Day')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Diurnal Temperature Pattern')
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()
```

### Weekly Patterns

```python
# Extract day of week
df['day_of_week'] = df.index.day_name()

# Calculate daily averages
daily_pattern = df.groupby('day_of_week')[['temperature', 'humidity']].mean()

# Reorder days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_pattern = daily_pattern.reindex(day_order)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(range(len(daily_pattern)), daily_pattern['temperature'])
ax.set_xticks(range(len(daily_pattern)))
ax.set_xticklabels(day_order, rotation=45)
ax.set_ylabel('Average Temperature (°C)')
ax.set_title('Weekly Temperature Pattern')
plt.tight_layout()
plt.show()
```

## Comparative Analysis

### Before/After Comparison

```python
# Split data
date_cutoff = pd.Timestamp('2026-05-15')
before = df[df.index < date_cutoff]
after = df[df.index >= date_cutoff]

# Compare statistics
print("Before Cutoff:")
print(before['temperature'].describe())
print("\nAfter Cutoff:")
print(after['temperature'].describe())

# T-test
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(before['temperature'], after['temperature'])
print(f"\nT-test p-value: {p_value:.4f}")
```

## Exporting Results

### Save to CSV

```python
# Save processed data
hourly_avg.to_csv('processed_data.csv')

# Save statistics
stats_df = df.describe().T
stats_df.to_csv('statistics.csv')
```

### Generate Report

```python
# Create summary report
report = f"""
Environmental Data Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Temperature Analysis:
  Mean: {df['temperature'].mean():.2f}°C
  Std Dev: {df['temperature'].std():.2f}°C
  Min: {df['temperature'].min():.2f}°C
  Max: {df['temperature'].max():.2f}°C
  Range: {df['temperature'].max() - df['temperature'].min():.2f}°C

Humidity Analysis:
  Mean: {df['humidity'].mean():.2f}%
  Std Dev: {df['humidity'].std():.2f}%
  Min: {df['humidity'].min():.2f}%
  Max: {df['humidity'].max():.2f}%

Pressure Analysis:
  Mean: {df['pressure'].mean():.2f} hPa
  Std Dev: {df['pressure'].std():.2f} hPa
  Min: {df['pressure'].min():.2f} hPa
  Max: {df['pressure'].max():.2f} hPa
"""

with open('analysis_report.txt', 'w') as f:
    f.write(report)
```

## Advanced Techniques

### Machine Learning

```python
from sklearn.ensemble import IsolationForest

# Detect anomalies using Isolation Forest
iso_forest = IsolationForest(contamination=0.1)
anomalies = iso_forest.fit_predict(df[['temperature', 'humidity', 'pressure']])

print(f"Detected {sum(anomalies == -1)} anomalies")
```

### Forecasting

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Fit exponential smoothing model
model = ExponentialSmoothing(df['temperature'], seasonal_periods=24, trend='add')
fit = model.fit()

# Forecast next 24 hours
forecast = fit.forecast(steps=24)
print(forecast)
```

## Next Steps

- Review [[Data Collection]] for understanding data sources
- Check [[Software Components]] for analysis tools setup
- Explore [[Hardware Setup]] for sensor specifications

## References

- [Pandas Documentation](https://pandas.pydata.org/)
- [NumPy Documentation](https://numpy.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Scikit-learn](https://scikit-learn.org/)
