
from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
print("Fetching data...")
cdc_diabetes_health_indicators = fetch_ucirepo(id=891) 
  
# data (as pandas dataframes) 
X = cdc_diabetes_health_indicators.data.features 
y = cdc_diabetes_health_indicators.data.targets 

print("Data fetched.")
print(f"Features shape: {X.shape}")
print(f"Targets shape: {y.shape}")

# Combine into one dataframe for export
df = pd.concat([X, y], axis=1)

# Export to CSV
output_file = "diabetes_data.csv"
print(f"Exporting to {output_file}...")
df.to_csv(output_file, index=False)
print("Done.")
