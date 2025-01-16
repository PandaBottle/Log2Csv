# Python program to convert
# JSON file to CSV
 
import json
import csv
import pandas as pd
import re

# Load JSON data from file
with open('data.json') as json_file:
    data = json.load(json_file)

# Function to extract parameters from HTTP status and Referer
def extract_params(http_status, referer):
    params = {'HTTP UID': '', 'Referer UID': ''}
    
    # Extract the URL from the HTTP status
    url_match = re.search(r'^(GET|POST) (.+?) HTTP\/\d+\.\d+$', http_status)
    if url_match:
        url = url_match.group(2)  # Get the URL part
        uid_match = re.search(r'uid=(.*?)(&|$)', url)
        if uid_match:
            params['HTTP UID'] = uid_match.group(1)  # Store UID from HTTP status

    # Check the Referer for UID
    if referer:
        uid_match_referer = re.search(r'uid=(.*?)(&|$)', referer)
        if uid_match_referer:
            params['Referer UID'] = uid_match_referer.group(1)  # Store UID from Referer

    return params

# Convert JSON to DataFrame
df = pd.DataFrame(data).T

# Extract parameters and add them to DataFrame
df['Extracted Params'] = df.apply(lambda row: extract_params(row['HTTP status'], row['Referer']), axis=1)
df = pd.concat([df.drop('Extracted Params', axis=1), df['Extracted Params'].apply(pd.Series)], axis=1)


# Reorder columns
df = df[['IP address', 'Time Stamp', 'HTTP status', 'HTTP UID', 'Return status', 'Referer','Referer UID','Browser Info']]

# Save DataFrame to CSV
df.to_csv("output_with_params.csv", index=False)