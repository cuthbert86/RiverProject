import pandas as pd

# Load your data from a CSV file (adjust the filename and path accordingly)
file_path = 'riverdatacsv.csv'
df = pd.read_csv(file_path)

# Merge Date and Time columns into a single DateTime column with the ISO 8601 format
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time']).dt.strftime('%Y-%m-%dT%H:%M:%S')

# Drop the original Date and Time columns if needed
df = df.drop(['Date', 'Time'], axis=1)

# Display the DataFrame with the new DateTime column
print(df)

# in future use this python command :  
# from datetime import datetime
# timestamp = datetime.now().isoformat()
