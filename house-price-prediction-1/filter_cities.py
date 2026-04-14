import pandas as pd
import os
import sys

# Change to script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Read the CSV file
df = pd.read_csv('data/house_prices.csv')
print(f"Original data: {len(df)} rows")

# Define priority cities (Metro and major populated cities)
# Tier 1 Metro Cities
tier1_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', 
    'Hyderabad', 'Pune', 'Ahmedabad'
]

# Tier 2 Major Cities (highly populated and popular)
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
    'Kolhapur', 'Sangli', 'Belagavi', 'Ballari', 'Shivamogga',
    'Kozhikode', 'Thrissur', 'Kollam', 'Palakkad', 'Kannur',
    'Gwalior', 'Ujjain', 'Rewa', 'Bhilai', 'Durg', 'Korba',
    'Bilaspur', 'Jalandhar', 'Patiala', 'Mohali', 'Bathinda',
    'Hisar', 'Panipat', 'Karnal', 'Rohtak', 'Ambala', 'Yamunanagar',
    'Siliguri', 'Durgapur', 'Asansol', 'Kharagpur', 'Haldia',
    'Howrah', 'Malda', 'Rourkela', 'Sambalpur', 'Balasore',
    'Tirupati', 'Nellore', 'Kurnool', 'Rajahmundry', 'Kadapa',
    'Guwahati', 'Dibrugarh', 'Jorhat', 'Tinsukia', 'Nagaon'
]

# Combine all priority cities
priority_cities = tier1_cities + tier2_cities

# Filter data: First get all priority cities
filtered_df = df[df['City'].isin(priority_cities)].copy()

# If we have less than 100 rows, add more cities to reach 100
if len(filtered_df) < 100:
    # Get remaining cities sorted by state (to get diverse representation)
    remaining_df = df[~df['City'].isin(priority_cities)].copy()
    
    # Sort by state to get diverse representation
    remaining_df = remaining_df.sort_values('State')
    
    # Add cities until we reach 100
    needed = 100 - len(filtered_df)
    additional_cities = remaining_df.head(needed)
    filtered_df = pd.concat([filtered_df, additional_cities], ignore_index=True)

# If we have more than 100 rows, prioritize and keep top 100
elif len(filtered_df) > 100:
    # Sort by priority: Tier 1 first, then Tier 2, then others
    filtered_df['priority'] = filtered_df['City'].apply(
        lambda x: 1 if x in tier1_cities else (2 if x in tier2_cities else 3)
    )
    filtered_df = filtered_df.sort_values(['priority', 'State', 'City'])
    filtered_df = filtered_df.head(100)
    filtered_df = filtered_df.drop('priority', axis=1)

# Reset index
filtered_df = filtered_df.reset_index(drop=True)

# Save to CSV
output_path = 'data/house_prices.csv'
filtered_df.to_csv(output_path, index=False)

print(f"\n{'='*60}")
print(f"Filtered data saved to {output_path}")
print(f"Total rows: {len(filtered_df)}")
print(f"\nTier 1 Metro Cities included: {len(filtered_df[filtered_df['City'].isin(tier1_cities)])}")
print(f"Tier 2 Major Cities included: {len(filtered_df[filtered_df['City'].isin(tier2_cities)])}")
print(f"\nSample of filtered cities (first 20):")
print(filtered_df[['State', 'City']].head(20).to_string(index=False))
print(f"\nSample of filtered cities (last 10):")
print(filtered_df[['State', 'City']].tail(10).to_string(index=False))
sys.stdout.flush()

