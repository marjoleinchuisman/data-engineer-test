import json
import pandas as pd

# Load the JSON data from the file
with open('eenvandaag_page_metrics.json', 'r') as json_file:
    data = json.load(json_file)

# Initialize empty lists to store the data
names = []
periods = []
end_times = []
values = []

# Iterate through the data and extract the required information
for entry in data['data']:
    name = entry['name']
    period = entry['period']
    
    # Check if the 'values' key exists and is a list
    if 'values' in entry and isinstance(entry['values'], list):
        for value_entry in entry['values']:
            end_time = value_entry.get('end_time', '')
            value = value_entry['value']
            
            # If value is a dictionary, sum its values
            if isinstance(value, dict):
                value = sum(value.values())
            
            names.append(name)
            periods.append(period)
            end_times.append(end_time)
            values.append(value)
    else:
        # Handle cases where 'values' is missing or not a list
        names.append(name)
        periods.append(period)
        end_times.append('')
        values.append('')

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'name': names,
    'period': periods,
    'end_time': end_time,
    'value': values,
})

# Save the DataFrame as a CSV file
df.to_csv('eenvandaag_metrics.csv', index=False)

# Test if CSV file has been created
print(f"CSV file has been created.")
