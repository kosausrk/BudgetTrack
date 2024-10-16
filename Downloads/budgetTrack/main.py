import csv

# Dictionary to store the total amount for each store
store_totals = {}

# Preset stores to combine
preset_stores = {
    "Amazon": ["AMAZON", "AMZN.COM", "WWW.AMAZON"],
    "Target": ["TARGET"],
    "Spotify": ["SPOTIFY"],
    "Apple": ["APPLE.COM", "APPLE"],
    "Netflix": ["NETFLIX"],
    "Chick-fil-A": ["CHICK-FIL-A"],
    "Subway": ["SUBWAY"],
    "CitiBike": ["CITIBIK"]
}

# Function to match store names to preset categories
def get_store_category(store_name):
    store_name_upper = store_name.upper()
    for category, keywords in preset_stores.items():
        if any(keyword in store_name_upper for keyword in keywords):
            return category
    return store_name  # Return the original store name if no match

# Open and read the CSV file
with open("/Users/koushiksarkar/Desktop/budgetTrack/bofa-data.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header line if there is one, or remove if not needed

    for row in reader:
        # Check if the row has at least 3 columns (store name and amount)
        if len(row) < 3:
            print(f"Skipping malformed row: {row}")
            continue  # Skip this row if it doesn't have at least 3 columns

        store_name = row[1]  # Store name or description is in the second column
        amount_str = row[2].replace(',', '')  # Remove commas from the amount string

        try:
            amount = float(amount_str)  # Convert the cleaned string to a float
        except ValueError:
            print(f"Error converting amount for row: {row}")
            continue  # Skip rows that can't be converted to float

        # Get the store category (preset or the original name)
        store_category = get_store_category(store_name)

        # If the store doesn't exist in the dictionary, add it with the current amount
        if store_category not in store_totals:
            store_totals[store_category] = amount
        else:
            # If it exists, update the total
            store_totals[store_category] += amount

# Output the totals for each store
for store, total in store_totals.items():
    print(f"{store}: ${total:.2f} \n \n ")
