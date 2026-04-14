#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os

# Read the CSV file
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'house_prices.csv')
df = pd.read_csv(csv_path)

max_price_limit = 30000000  # 3 crores
max_price = df['Price'].max()
min_price = df['Price'].min()

print(f"{'='*60}")
print(f"Data Verification Report")
print(f"{'='*60}")
print(f"Total rows: {len(df)}")
print(f"Maximum price: ₹{max_price:,} ({max_price/10000000:.2f} crores)")
print(f"Minimum price: ₹{min_price:,} ({min_price/10000000:.2f} crores)")
print(f"\nPrice limit check: ₹{max_price_limit:,} (3 crores)")
print(f"All prices <= 3 crores: {'✓ YES' if max_price <= max_price_limit else '✗ NO'}")

if max_price > max_price_limit:
    print(f"\n⚠️  WARNING: Found {len(df[df['Price'] > max_price_limit])} rows exceeding 3 crores!")
    print("\nRows exceeding limit:")
    print(df[df['Price'] > max_price_limit][['City', 'Price']].to_string(index=False))
else:
    print(f"\n✓ All {len(df)} rows are within the 3 crores limit!")

print(f"\nTop 5 highest prices:")
top5 = df.nlargest(5, 'Price')[['City', 'State', 'Price']]
for idx, row in top5.iterrows():
    price_crores = row['Price'] / 10000000
    print(f"  {row['City']:20s} ({row['State']:20s}) - ₹{row['Price']:,} ({price_crores:.2f} crores)")


