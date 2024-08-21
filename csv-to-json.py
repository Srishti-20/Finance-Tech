import pandas as pd
import json
import math

# Load CSV file
csv_file = '/Users/2003s/Downloads/HSBC.csv'
df = pd.read_csv(csv_file)

# Clean up the strings in the DataFrame (if needed)
def clean_string(s):
    if isinstance(s, str):
        s = s.strip("'\"")
    return s

for column in df.select_dtypes(include='object').columns:
    df[column] = df[column].apply(clean_string)

# Convert DataFrame to JSON
json_data = df.to_dict(orient='records')

# Define the number of chunks (adjust this based on your needs)
number_of_chunks = 6  # For example, if you want 10 chunks

# Calculate chunk size
chunk_size = math.ceil(len(json_data) / number_of_chunks)

# Split data into chunks
chunks = [json_data[i:i + chunk_size] for i in range(0, len(json_data), chunk_size)]

# Save chunks to individual JSON files
for i, chunk in enumerate(chunks):
    with open(f'data_chunk_{i + 1}.json', 'w') as json_file:
        json.dump(chunk, json_file, indent=4)
