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

# Define priority cities (Metro and major populated cities)
tier1_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', 
    'Hyderabad', 'Pune', 'Ahmedabad'
]

tier2_cities = [
    'Surat', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 
    'Vadodara', 'Visakhapatnam', 'Coimbatore', 'Patna', 'Bhopal',
    'Thane', 'Gurugram', 'Faridabad', 'Noida', 'Meerut', 'Rajkot',
    'Jabalpur', 'Dhanbad', 'Amritsar', 'Ludhiana', 'Kochi', 
    'Thiruvananthapuram', 'Mysuru', 'Mangaluru', 'Hubballi',
    'Nashik', 'Aurangabad', 'Solapur', 'Raipur', 'Jamshedpur',
    'Ranchi', 'Bhubaneswar', 'Cuttack', 'Vijayawada', 'Guntur',
    'Warangal', 'Salem', 'Madurai', 'Trichy', 'Varanasi', 'Agra',
    'Prayagraj', 'Gorakhpur', 'Jhansi', 'Dehradun', 'Haridwar',
    'Udaipur', 'Jodhpur', 'Kota', 'Ajmer', 'Bikaner', 'Amravati',
    'Kolhapur', 'Belagavi', 'Ballari', 'Shivamogga',
    'Kozhikode', 'Thrissur', 'Kollam', 'Palakkad', 'Kannur',
    'Gwalior', 'Ujjain', 'Rewa', 'Bhilai', 'Durg', 'Korba',
    'Bilaspur', 'Jalandhar', 'Patiala', 'Mohali', 'Bathinda',
    'Hisar', 'Panipat', 'Karnal', 'Rohtak', 'Ambala', 'Yamunanagar',
    'Siliguri', 'Durgapur', 'Asansol', 'Kharagpur', 'Haldia',
    'Howrah', 'Malda', 'Rourkela', 'Sambalpur', 'Balasore',
    'Tirupati', 'Nellore', 'Kurnool', 'Rajahmundry', 'Kadapa',
    'Guwahati', 'Dibrugarh', 'Jorhat', 'Tinsukia', 'Nagaon'
]

priority_cities = tier1_cities + tier2_cities

# Filter data: First get all priority cities
filtered_df = df[df['City'].isin(priority_cities)].copy()
print(f"Priority cities found: {len(filtered_df)} rows")

# If we have less than 100 rows, add more cities
if len(filtered_df) < 100:
    remaining_df = df[~df['City'].isin(priority_cities)].copy()
    remaining_df = remaining_df.sort_values('State')
    needed = 100 - len(filtered_df)
    additional_cities = remaining_df.head(needed)
    filtered_df = pd.concat([filtered_df, additional_cities], ignore_index=True)
    print(f"Added {needed} more cities to reach 100")

# If we have more than 100 rows, prioritize and keep top 100
elif len(filtered_df) > 100:
    filtered_df['priority'] = filtered_df['City'].apply(
        lambda x: 1 if x in tier1_cities else (2 if x in tier2_cities else 3)
    )
    filtered_df = filtered_df.sort_values(['priority', 'State', 'City'])
    filtered_df = filtered_df.head(100)
    filtered_df = filtered_df.drop('priority', axis=1)
    print(f"Reduced to top 100 priority cities")

# Reset index
filtered_df = filtered_df.reset_index(drop=True)

# Save to CSV
filtered_df.to_csv(csv_path, index=False)

print(f"\n{'='*60}")
print(f"SUCCESS: Filtered data saved to {csv_path}")
print(f"Total rows: {len(filtered_df)}")
print(f"Tier 1 Metro Cities: {len(filtered_df[filtered_df['City'].isin(tier1_cities)])}")
print(f"Tier 2 Major Cities: {len(filtered_df[filtered_df['City'].isin(tier2_cities)])}")
print(f"\nFirst 10 cities:")
for idx, row in filtered_df.head(10).iterrows():
    print(f"  {row['State']:20s} - {row['City']:20s}")


