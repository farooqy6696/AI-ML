# ==========================================
# PROJECT 4 - HOUSE SALES DATA ANALYSIS
# ==========================================


# ==========================================
# IMPORT LIBRARIES
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# ==========================================
# FILE PATHS
# ==========================================

# Get the folder where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset path
DATA_FILE = os.path.join(
    BASE_DIR,
    "kc_house_data.csv"
)

# Graph folder path
GRAPH_DIR = os.path.join(
    BASE_DIR,
    "Graphs"
)

# Create Graphs folder if it does not exist
os.makedirs(
    GRAPH_DIR,
    exist_ok=True
)


# ==========================================
# SCENARIO 1
# DATA LOADING & BASIC CLEANING
# ==========================================

print("\n==========================================")
print("SCENARIO 1: DATA LOADING & BASIC CLEANING")
print("==========================================")

# ------------------------------------------
# Task 1: Load the dataset
# ------------------------------------------

df = pd.read_csv(DATA_FILE)


# ------------------------------------------
# Task 2: Display first 5 rows
# ------------------------------------------

print("\nFirst 5 Rows:")
print(df.head())


# Display column names
print("\nColumn Names:")
print(df.columns)


# ------------------------------------------
# Task 3: Convert required columns to numeric
# ------------------------------------------

df["bedrooms"] = pd.to_numeric(
    df["bedrooms"],
    errors="coerce"
)

df["bathrooms"] = pd.to_numeric(
    df["bathrooms"],
    errors="coerce"
)

df["sqft_living"] = pd.to_numeric(
    df["sqft_living"],
    errors="coerce"
)

df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)


# ------------------------------------------
# Task 4: Check missing values
# ------------------------------------------

print("\nMissing Values Before Filling:")

print(
    "bedrooms:",
    df["bedrooms"].isnull().sum()
)

print(
    "bathrooms:",
    df["bathrooms"].isnull().sum()
)

print(
    "sqft_living:",
    df["sqft_living"].isnull().sum()
)

print(
    "price:",
    df["price"].isnull().sum()
)


# ------------------------------------------
# Task 5: Fill missing values
# ------------------------------------------

# bedrooms → mode
df["bedrooms"] = df["bedrooms"].fillna(
    df["bedrooms"].mode()[0]
)

# bathrooms → mean
df["bathrooms"] = df["bathrooms"].fillna(
    df["bathrooms"].mean()
)

# sqft_living → mean
df["sqft_living"] = df["sqft_living"].fillna(
    df["sqft_living"].mean()
)

# price → mean
df["price"] = df["price"].fillna(
    df["price"].mean()
)


# ------------------------------------------
# Final missing-value check
# ------------------------------------------

print("\nMissing Values After Filling:")

print(
    "bedrooms:",
    df["bedrooms"].isnull().sum()
)

print(
    "bathrooms:",
    df["bathrooms"].isnull().sum()
)

print(
    "sqft_living:",
    df["sqft_living"].isnull().sum()
)

print(
    "price:",
    df["price"].isnull().sum()
)


print("\nScenario 1 completed successfully!")


# ==========================================
# SCENARIO 2
# LINE GRAPH + SAVE
# ==========================================

print("\n==========================================")
print("SCENARIO 2: LINE GRAPH + SAVE")
print("==========================================")


# ------------------------------------------
# Task 1 & 2:
# Select id and price and take first 10 rows
# ------------------------------------------

line_df = df[
    ["id", "price"]
].head(10)


print("\nFirst 10 House Prices:")
print(line_df)


# ------------------------------------------
# Task 3:
# Convert price to NumPy array
# ------------------------------------------

price_array = line_df[
    "price"
].to_numpy()


print("\nPrice NumPy Array:")
print(price_array)


# ------------------------------------------
# Task 4:
# Create line graph
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    price_array,
    marker="o"
)


# ------------------------------------------
# Task 5:
# Add title and labels
# ------------------------------------------

plt.title(
    "House Prices of First 10 Records"
)

plt.xlabel(
    "Index"
)

plt.ylabel(
    "Price"
)


plt.tight_layout()


# ------------------------------------------
# Task 6:
# Save line graph
# ------------------------------------------

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "house_prices_line.png"
    ),
    dpi=150
)


# Display graph
plt.show()

# Close graph
plt.close()


print("\nScenario 2 completed successfully!")


# ==========================================
# SCENARIO 3
# FILTERING + BAR CHART + SAVE
# ==========================================

print("\n==========================================")
print("SCENARIO 3: FILTERING + BAR CHART + SAVE")
print("==========================================")


# ------------------------------------------
# Task 1:
# Filter houses where price > 1,000,000
# ------------------------------------------

expensive_houses = df[
    df["price"] > 1000000
]


print("\nNumber of Expensive Houses:")
print(
    len(expensive_houses)
)


# ------------------------------------------
# Count houses by bedrooms
# ------------------------------------------

bedrooms_counts = expensive_houses[
    "bedrooms"
].value_counts()


print("\nExpensive Houses by Bedrooms:")
print(bedrooms_counts)


# ------------------------------------------
# Task 2:
# Select top bedroom categories
# ------------------------------------------

top_bedrooms = bedrooms_counts.head(5)


print("\nTop Bedroom Categories:")
print(top_bedrooms)


# ------------------------------------------
# Task 3:
# Convert results to NumPy arrays
# ------------------------------------------

x = top_bedrooms.index.to_numpy()

y = top_bedrooms.values


print("\nBedrooms NumPy Array:")
print(x)

print("\nHouse Count NumPy Array:")
print(y)


# ------------------------------------------
# Task 4:
# Create bar chart
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    x,
    y
)


# ------------------------------------------
# Task 5:
# Add title and labels
# ------------------------------------------

plt.title(
    "Expensive Houses by Bedrooms"
)

plt.xlabel(
    "Bedrooms"
)

plt.ylabel(
    "Count"
)


plt.tight_layout()


# ------------------------------------------
# Task 6:
# Save bar chart
# ------------------------------------------

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "expensive_houses_bar.png"
    ),
    dpi=150
)


# Display graph
plt.show()

# Close graph
plt.close()


print("\nScenario 3 completed successfully!")


# ==========================================
# PROJECT 4 - SCENARIOS 1 TO 3 COMPLETED
# ==========================================

print("\n==========================================")
print("SCENARIOS 1, 2 AND 3 COMPLETED!")
print("==========================================")

# ==========================================
# SCENARIO 4
# PIE CHART (BEDROOM DISTRIBUTION) + SAVE
# ==========================================

print("\n==========================================")
print("SCENARIO 4: PIE CHART - BEDROOM DISTRIBUTION")
print("==========================================")


# ------------------------------------------
# Task 1:
# Count the number of houses by bedrooms
# ------------------------------------------

bedroom_counts = df["bedrooms"].value_counts()

print("\nHouse Count by Bedrooms:")
print(bedroom_counts)


# ------------------------------------------
# Task 2:
# Select top 5 bedroom categories
# ------------------------------------------

top_bedrooms = bedroom_counts.head(5)

print("\nTop 5 Bedroom Categories:")
print(top_bedrooms)


# ------------------------------------------
# Task 3:
# Prepare labels and values
# ------------------------------------------

labels = top_bedrooms.index.astype(str)

values = top_bedrooms.values


print("\nLabels:")
print(labels)

print("\nValues:")
print(values)


# ------------------------------------------
# Task 4:
# Create Pie Chart
# ------------------------------------------

plt.figure(figsize=(8, 8))

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)


# ------------------------------------------
# Task 5:
# Add title
# ------------------------------------------

plt.title(
    "Bedroom Distribution - Top 5 Categories"
)


plt.tight_layout()


# ------------------------------------------
# Task 6:
# Save Pie Chart
# ------------------------------------------

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "bedroom_distribution.png"
    ),
    dpi=150
)


# Display graph
plt.show()


# Close graph
plt.close()


print("\nScenario 4 completed successfully!")

# ==========================================
# SCENARIO 5
# ADVANCED ANALYSIS + MULTIPLE GRAPHS
# ==========================================

print("\n==========================================")
print("SCENARIO 5: ADVANCED ANALYSIS + MULTIPLE GRAPHS")
print("==========================================")


# ==========================================
# PART 1: FEATURE CREATION
# ==========================================

print("\n========== PART 1: PRICE CATEGORY ==========")

# Make sure price is numeric
df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)


# Create Price Category
def categorize_price(price):

    if price >= 1000000:
        return "Luxury"

    elif price >= 500000:
        return "Mid Range"

    else:
        return "Affordable"


# Apply the function to price column
df["price_category"] = df["price"].apply(
    categorize_price
)


# Display Price Category counts
print("\nPrice Category Counts:")

print(
    df["price_category"].value_counts()
)


# ==========================================
# PART 2: NUMPY USAGE
# ==========================================

print("\n========== PART 2: NUMPY ANALYSIS ==========")


# Convert price column to NumPy array
price_array = df["price"].to_numpy()


print("\nPrice NumPy Array:")
print(price_array[:10])


# Calculate price differences using np.diff()
price_diff = np.diff(price_array)


print("\nFirst 10 Price Differences:")
print(price_diff[:10])


# Display basic information
print("\nNumber of Price Differences:")
print(len(price_diff))


# ==========================================
# PART 3: VISUALIZATIONS
# ==========================================


# ------------------------------------------
# 1. LINE GRAPH
# House Price Trend
# ------------------------------------------

print("\nCreating Price Trend Line Graph...")


# Remove missing prices
price_array = df["price"].dropna().to_numpy()


plt.figure(figsize=(10, 5))


plt.plot(
    price_array,
    marker="o",
    markersize=2,
    linewidth=1
)


plt.title(
    "House Price Trend"
)

plt.xlabel(
    "Index"
)

plt.ylabel(
    "Price"
)


plt.tight_layout()


# Save line graph
plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "price_trend.png"
    ),
    dpi=150
)


plt.show()

plt.close()


print(
    "price_trend.png saved successfully!"
)


# ------------------------------------------
# 2. STACKED BAR CHART
# Price Category by Bedrooms
# ------------------------------------------

print("\nCreating Stacked Bar Chart...")


# Make sure bedrooms is numeric
df["bedrooms"] = pd.to_numeric(
    df["bedrooms"],
    errors="coerce"
)


# Round bedroom values
df["bedrooms"] = df["bedrooms"].round()


# Remove missing bedroom values
df = df.dropna(
    subset=["bedrooms"]
)


# Keep reasonable bedroom categories
df = df[
    df["bedrooms"] <= 10
]


# Group by bedrooms and price category
stack_data = df.groupby(
    [
        "bedrooms",
        "price_category"
    ]
).size().unstack(
    fill_value=0
)


# Select top 5 bedroom categories
stack_data = stack_data.head(5)


print("\nStacked Bar Chart Data:")
print(stack_data)


# Create stacked bar chart
stack_data.plot(
    kind="bar",
    figsize=(10, 6),
    stacked=True
)


plt.title(
    "Price Category Distribution by Bedrooms"
)

plt.xlabel(
    "Bedrooms"
)

plt.ylabel(
    "Count"
)


plt.xticks(
    rotation=0
)

plt.legend(
    title="Price Category"
)


plt.tight_layout()


# Save stacked bar chart
plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "price_category_stacked.png"
    ),
    dpi=150
)


plt.show()

plt.close()


print(
    "price_category_stacked.png saved successfully!"
)


# ------------------------------------------
# 3. HISTOGRAM
# Price Distribution
# ------------------------------------------

print("\nCreating Price Histogram...")


# Remove extreme 5% values
# to make the distribution easier to see
upper_limit = df["price"].quantile(0.95)


filtered_prices = df[
    df["price"] <= upper_limit
]["price"]


plt.figure(figsize=(10, 5))


plt.hist(
    filtered_prices,
    bins=30
)


plt.title(
    "Price Distribution"
)

plt.xlabel(
    "Price"
)

plt.ylabel(
    "Frequency"
)


# Display normal numbers instead of scientific notation
plt.ticklabel_format(
    style="plain",
    axis="x"
)


plt.tight_layout()


# Save histogram
plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "price_histogram.png"
    ),
    dpi=150
)


plt.show()

plt.close()


print(
    "price_histogram.png saved successfully!"
)


# ==========================================
# PART 5: REQUIRED INSIGHTS
# ==========================================

print("\n==========================================")
print("PART 5: INSIGHTS")
print("==========================================")


# ------------------------------------------
# Insight 1:
# Which bedroom category has the most
# expensive houses?
# ------------------------------------------

luxury_houses = df[
    df["price_category"] == "Luxury"
]


if not luxury_houses.empty:

    top_bedroom = (
        luxury_houses["bedrooms"]
        .value_counts()
        .idxmax()
    )

    print(
        "\n1. Bedroom category with most expensive houses:",
        int(top_bedroom)
    )

else:

    print(
        "\n1. No Luxury houses found."
    )


# ------------------------------------------
# Insight 2:
# Which price category is most common?
# ------------------------------------------

common_category = (
    df["price_category"]
    .value_counts()
    .idxmax()
)


print(
    "2. Most common price category:",
    common_category
)


# ------------------------------------------
# Insight 3:
# What is the distribution pattern?
# ------------------------------------------

print(
    "3. Price distribution is right-skewed."
)

print(
    "   Most houses are concentrated in the lower "
    "price range, with fewer houses having very "
    "high prices."
)


# ==========================================
# SCENARIO 5 COMPLETED
# ==========================================

print("\n==========================================")
print("SCENARIO 5 COMPLETED SUCCESSFULLY!")
print("==========================================")