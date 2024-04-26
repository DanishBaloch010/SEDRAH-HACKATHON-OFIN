import pandas as pd
import re

# Function to parse the extracted text and create a DataFrame
def parse_text_to_dataframe(text):
    lines = text.split("\n")
    data = {"Category": [], "Amount_2022": [], "Amount_2021": []}  # Changed column names
    current_category = None

    for line in lines:
        if re.match(r"^\w+ Inc\.$", line):  # Company name
            company_name = line
        elif re.match(r"CONDENSED CONS", line):  # Start of financial statements
            current_category = line
        elif current_category:
            match = re.match(r"([A-Za-z\s]+)\s+(\d+(?:,\d{3})*(?:\.\d+)?)\s+(\d+(?:,\d{3})*(?:\.\d+)?)$", line)
            if match:
                category, amount_2022, amount_2021 = match.groups()
                data["Category"].append(category.strip())
                data["Amount_2022"].append(amount_2022.strip())  # Added Amount_2022 to data
                data["Amount_2021"].append(amount_2021.strip())  # Added Amount_2021 to data

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

# Read the text file
with open('extracted_text.txt', 'r') as file:
    extracted_text = file.read()

# Parse the text and create DataFrame
df = parse_text_to_dataframe(extracted_text)
df.to_csv('dataframe.csv')
