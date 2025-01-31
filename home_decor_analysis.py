import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 1. Onboarding Data for Analysis
# Sample data for home decor products (manually created)
data = [
    {"id": 1, "title": "Modern Lamp", "price": 25.99, "description": "Stylish modern table lamp", "category": "home decor", "image": "", "rating": 4.5},
    {"id": 2, "title": "Wall Clock", "price": 15.50, "description": "Elegant wall clock", "category": "home decor", "image": "", "rating": 4.0},
    {"id": 3, "title": "Sofa Set", "price": 499.99, "description": "Comfortable 3-seater sofa", "category": "home decor", "image": "", "rating": 4.2},
    {"id": 4, "title": "Area Rug", "price": 45.75, "description": "Soft and plush area rug", "category": "home decor", "image": "", "rating": 4.7},
    {"id": 5, "title": "Decorative Mirror", "price": 60.00, "description": "Vintage decorative mirror", "category": "home decor", "image": "", "rating": 4.3}
] 

# Creating DataFrame
df = pd.DataFrame(data)

# Filter home decor related products based on keywords
home_decor_keywords = ["lamp", "clock", "sofa", "cushion", "rug", "mirror", "wall art"]
df_home_decor = df[df["title"].str.contains('|'.join(home_decor_keywords), case=False, na=False)]

# Save the data to CSV for record-keeping
today = datetime.today().strftime('%Y-%m-%d')
df_home_decor.to_csv(f"home_decor_data_{today}.csv", index=False)

# Output DataFrame to check
if df_home_decor.empty:
    print("No home decor products found.")
else:
    print(f"Filtered Home Decor Products ({len(df_home_decor)}):")
    print(df_home_decor.head())

# Debugging: Print available categories
print("Available Categories:", df["category"].unique())

# 2. Customer Behavior Analysis
if 'price' in df_home_decor.columns and not df_home_decor['price'].isnull().any():
    plt.figure(figsize=(8, 6))
    sns.histplot(df_home_decor['price'], bins=20, kde=True)
    plt.title("Price Distribution of Home Decor Products")
    plt.xlabel("Price (Rs)")
    plt.ylabel("Frequency")
    plt.show()
else:
    print("No valid price data to analyze.")

# Example: Generating Insights on Price Range
if 'price' in df_home_decor.columns:
    price_range = df_home_decor['price'].quantile([0.25, 0.5, 0.75])
    print(f"Price Range (25th, 50th, 75th percentiles): {price_range}")
else:
    print("Price data is missing or invalid in home decor products.")

# 3. Competitor Analysis (assuming 'competitor_data.csv' contains competitor information)
try:
    competitor_df = pd.read_csv("competitor_data.csv")

    # Check if required columns exist
    required_columns = ['brand', 'price', 'ratings']
    if all(col in competitor_df.columns for col in required_columns):
        competitor_summary = competitor_df.groupby('brand')[['price', 'ratings']].mean()
        print("Competitor Analysis Summary:")
        print(competitor_summary)

        # Visualization: Competitor Price Comparison
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=competitor_df['brand'], y=competitor_df['price'])
        plt.title("Competitor Price Comparison")
        plt.xlabel("Brand")
        plt.ylabel("Price ($)")
        plt.xticks(rotation=45)
        plt.show()

    else:
        print("Missing required columns in competitor data.")
except FileNotFoundError:
    print("Competitor data file 'competitor_data.csv' not found. Please provide the data.")

# 4. Insights and Actionable Recommendations
if not competitor_df.empty:
    competitor_median_price = competitor_df['price'].median()
    home_decor_median_price = df_home_decor['price'].median()

    print(f"Competitor Median Price: ${competitor_median_price}")
    print(f"Home Decor Median Price: ${home_decor_median_price}")

    # Recommendation: Align pricing strategy with competitors if required
    if home_decor_median_price > competitor_median_price:
        print("Recommendation: Consider lowering the price to align with competitors.")
    else:
        print("Recommendation: Maintain current pricing strategy.")
else:
    print("No competitor data found for analysis.")

# 5. Saving insights to CSV files for record-keeping
price_range.to_csv("price_insights.csv")
competitor_summary.to_csv("competitor_summary.csv")
print("Market insights saved successfully!")
