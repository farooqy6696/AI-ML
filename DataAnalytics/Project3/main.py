import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------------------
# STEP 1: LOAD DATASET
# ------------------------------
df = pd.read_csv("scottish_hills.csv")


# ------------------------------
# STEP 2: CONVERT HEIGHT
# ------------------------------
df["Height"] = pd.to_numeric(df["Height"], errors='coerce')


# ------------------------------
# STEP 3: CREATE REGION COLUMN
# ------------------------------
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()


def assign_region(row):
    lat = row["Latitude"]
    lon = row["Longitude"]

    if lat >= lat_mid and lon >= lon_mid:
        return "North-East"

    elif lat >= lat_mid and lon < lon_mid:
        return "North-West"

    elif lat < lat_mid and lon >= lon_mid:
        return "South-East"

    else:
        return "South-West"


df["Region"] = df.apply(assign_region, axis=1)


# ------------------------------
# STEP 4: HANDLE MISSING VALUES
# ------------------------------

# Fill Height with mean
df["Height"] = df["Height"].fillna(df["Height"].mean())

# Fill Region with mode
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])


# ------------------------------
# STEP 5: OUTPUT
# ------------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ------------------------------
# SCENARIO 2: LINE GRAPH
# ------------------------------

# Step 1: Select required columns
data = df[['Hill Name', 'Height']]

# Step 2: Take first 10 rows
data_10 = data.head(10)

# Step 3: Convert Height to NumPy array
height_array = np.array(data_10['Height'])

# Step 4: Create line graph
plt.figure()
plt.plot(range(10), height_array, marker='o')

# Step 5: Add title and axis labels
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index (0–9)")
plt.ylabel("Height")
plt.tight_layout()

# Step 6: Save and display graph
plt.savefig("Graphs/hill_heights_line.png")
plt.show()

# ------------------------------
# SCENARIO 3: FILTERING + BAR CHART
# ------------------------------

# Step 1: Filter hills where Height > 900
tall_hills = df[df['Height'] > 900]

# Step 2: Count number of tall hills per Region
region_counts = tall_hills['Region'].value_counts()

# Step 3: Select top Regions
top_regions = region_counts.head()

# Step 4: Convert results into NumPy arrays
regions_array = np.array(top_regions.index)
counts_array = np.array(top_regions.values)

# Step 5: Create bar chart
plt.figure()
plt.bar(regions_array, counts_array)

# Step 6: Add title and axis labels
plt.title("Number of Tall Hills (>900m) per Region")
plt.xlabel("Region")
plt.ylabel("Count")

# Step 7: Adjust layout
plt.tight_layout()

# Step 8: Save the graph
plt.savefig("Graphs/tall_hills_bar.png")

# Step 9: Display the graph
plt.show()

# ------------------------------
# SCENARIO 4: PIE CHART
# ------------------------------

# Step 1: Count hills per Region
region_counts = df["Region"].value_counts()

# Step 2: Select top 5 regions
top_regions = region_counts.head(5)

# Step 3: Prepare labels and values
labels = top_regions.index
values = top_regions.values

# Step 4: Create pie chart
plt.figure(figsize=(10, 6))
plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140
)

# Step 5: Add title
plt.title("Distribution of Hills by Region")

# Adjust layout
plt.tight_layout()

# Step 6: Save the graph
plt.savefig("Graphs/region_distribution.png")

# Step 7: Display the graph
plt.show()

# ------------------------------
# SCENARIO 5: ADVANCED ANALYSIS
# ------------------------------

# ------------------------------
# PART 1: FEATURE CREATION
# ------------------------------

def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"


df["Height_Category"] = df["Height"].apply(height_category)


# ------------------------------
# PART 2: NUMPY USAGE
# ------------------------------

# Convert Height column to NumPy array
height_array = np.array(df["Height"])

# Calculate height differences
height_diff = np.diff(height_array)

print("\nFirst 10 Height Differences:")
print(height_diff[:10])


# ------------------------------
# PART 3: VISUALIZATIONS
# ------------------------------

# 1. Line Graph - Height Trend
plt.figure()

plt.plot(
    range(len(height_array)),
    height_array
)

plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")

plt.tight_layout()

plt.savefig(
    "Graphs/height_trend.png"
)

plt.show()


# 2. Stacked Bar Chart - Category per Region

category_region = pd.crosstab(
    df["Region"],
    df["Height_Category"]
)

category_region.plot(
    kind="bar",
    stacked=True
)

plt.title("Height Category Distribution per Region")
plt.xlabel("Region")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "Graphs/height_category_stacked.png"
)

plt.show()


# 3. Histogram - Height Distribution

plt.figure()

plt.hist(
    df["Height"],
    bins=10,
    edgecolor="black"
)

plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "Graphs/height_histogram.png"
)

plt.show()


# ------------------------------
# PART 4: INSIGHTS
# ------------------------------

# Find region with tallest average hills
tallest_region = df.groupby(
    "Region"
)["Height"].mean().idxmax()


# Find most common height category
common_category = df[
    "Height_Category"
].value_counts().idxmax()


print("\nInsights We Have Got Are:")

print(
    "Tallest Region (avg height):",
    tallest_region
)

print(
    "Most Common Height Category:",
    common_category
)