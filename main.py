# Import the pandas library as pd for data manipulation
import pandas as pd

# Read a CSV file named "Mobile phone price.csv" into a DataFrame named 'phone_csv_missing'
phone_csv_missing = pd.read_csv('Mobile phone price.csv')

# Drop rows with missing values and save to a new CSV file
phone_csv_missing = phone_csv_missing.dropna()
phone_csv_missing.to_csv('Cleaned data.csv')

# Read the original CSV file into a new DataFrame 'phone_csv'
phone_csv = pd.read_csv('Mobile phone price.csv')

# Fill missing values in 'Price ($)' column with the mean of the column
phone_csv['Price ($)'].fillna(phone_csv['Price ($)'].mean(), inplace=True)

# Clean 'Storage' and 'RAM' columns by removing 'GB' and converting to integers
phone_csv['Storage '] = phone_csv['Storage '].str.replace('GB', '').str.replace(' ', '').astype(int)
phone_csv['RAM '] = phone_csv['RAM '].str.replace('GB', '').str.replace(' ', '').astype(int)

# Create a new column 'New Col' filled with value 1
phone_csv['New Col'] = 1

# Create a new column 'Product' by multiplying 'Storage' and 'RAM'
phone_csv['Product'] = phone_csv['Storage '] * phone_csv['RAM ']

# Create a new column 'Safe' filled with boolean value True
phone_csv['Safe'] = True

# Drop the 'New Col' column
phone_csv_drop = phone_csv.drop('New Col', axis=1)

# Randomly sample 50% of the rows and create a new DataFrame 'phone_csv_shuffle'
phone_csv_shuffle = phone_csv.sample(frac=0.5)

# Reset the index of 'phone_csv_shuffle'
phone_csv_reset = phone_csv_shuffle.reset_index(drop=True)

# Rename the column 'Storage ' to 'Storage (MB)' and multiply by 1000
phone_csv.rename(columns={'Storage ': 'Storage (MB)'}, inplace=True)
phone_csv['Storage (MB)'] = phone_csv['Storage (MB)'].apply(lambda x: x * 1000)
