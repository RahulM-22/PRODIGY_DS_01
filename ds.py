import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace the path with the location where your file is saved)
data_path = 'D:/MP 1 FINAL/DS 01/API_SP.POP.TOTL_DS2_en_csv_v2_3401680/API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv'  # Replace with actual path
df = pd.read_csv(data_path, skiprows=4)  # Skip the initial metadata rows if present

# Display the first few rows and column names to understand the structure of the dataset
print(df.head())
print(df.columns)  # Check the exact column names

# Check if the column for "2022" is named exactly as such
if '2022' not in df.columns:
    print("The column for the year 2022 might be named differently. Please verify the column names.")
    
# Filter or select relevant columns (e.g., country name and population)
df_filtered = df[['Country Name', '2022']]  # Adjust if the column name is different
df_filtered = df_filtered.dropna()  # Drop rows with missing values

# Sort the dataset by population for better visualization
df_sorted = df_filtered.sort_values(by='2022', ascending=False).head(10)  # Top 10 most populated countries

# Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='2022', y='Country Name', data=df_sorted, palette='viridis')
plt.title('Top 10 Most Populated Countries in 2022')
plt.xlabel('Population')
plt.ylabel('Country')
plt.show()
