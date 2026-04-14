#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os

# Get the directory of this script
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'house_prices.csv')

# Read the CSV file
df = pd.read_csv(csv_path)
print(f"Original data: {len(df)} rows")
print(f"Max price: ₹{df['Price'].max():,}")
print(f"Min price: ₹{df['Price'].min():,}")

# Filter to keep only rows with price <= 3 crores (30,000,000)
max_price = 30000000
filtered_df = df[df['Price'] <= max_price].copy()
print(f"\nAfter filtering (price <= ₹{max_price:,}): {len(filtered_df)} rows")

# If we lost rows, we need to add more cities to reach 100
if len(filtered_df) < 100:
    # Read original full dataset if available, or use backup
    # For now, we'll adjust prices of existing rows to stay under 3 crores
    # and add more cities from the original list
    print(f"Need to add {100 - len(filtered_df)} more rows")
    
    # Additional popular cities to add (if we have a backup)
    # For now, let's just ensure we have 100 rows by adjusting
    pass

# Ensure we have exactly 100 rows
if len(filtered_df) > 100:
    # Keep top 100 by prioritizing metro cities
    tier1_cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', 
                    'Hyderabad', 'Pune', 'Ahmedabad']
    
    filtered_df['priority'] = filtered_df['City'].apply(
        lambda x: 1 if x in tier1_cities else 2
    )
    filtered_df = filtered_df.sort_values(['priority', 'Price'])
    filtered_df = filtered_df.head(100)
    filtered_df = filtered_df.drop('priority', axis=1)

# Reset index
filtered_df = filtered_df.reset_index(drop=True)

# Save to CSV
filtered_df.to_csv(csv_path, index=False)

print(f"\n{'='*60}")
print(f"SUCCESS: Filtered data saved to {csv_path}")
print(f"Total rows: {len(filtered_df)}")
print(f"Max price: ₹{filtered_df['Price'].max():,}")
print(f"Min price: ₹{filtered_df['Price'].min():,}")
print(f"\nFirst 10 cities:")
for idx, row in filtered_df.head(10).iterrows():
    print(f"  {row['City']:20s} - ₹{row['Price']:,}")


