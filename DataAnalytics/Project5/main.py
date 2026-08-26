# ============================================================
#                 CARS DATA ANALYSIS
#                 SCENARIO 1
#          Data Loading & Basic Cleaning
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("cardata.csv")

print("=" * 60)
print("CARS DATA ANALYSIS - SCENARIO 1")
print("=" * 60)


# ------------------------------------------------------------
# 3. DISPLAY FIRST 5 ROWS
# ------------------------------------------------------------

print("\nFIRST 5 ROWS:")
print(df.head())


# ------------------------------------------------------------
# 4. DISPLAY LAST 5 ROWS
# ------------------------------------------------------------

print("\nLAST 5 ROWS:")
print(df.tail())


# ------------------------------------------------------------
# 5. DISPLAY COLUMN NAMES
# ------------------------------------------------------------

print("\nCOLUMN NAMES:")
print(df.columns)


# ------------------------------------------------------------
# 6. DISPLAY SHAPE OF DATASET
# ------------------------------------------------------------

print("\nSHAPE OF DATASET:")
print(df.shape)


# ------------------------------------------------------------
# 7. CHECK DATA TYPES
# ------------------------------------------------------------

print("\nDATA TYPES:")
print(df.dtypes)


# ------------------------------------------------------------
# 8. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMISSING VALUES:")
print(df[
    [
        "Selling_Price",
        "Present_Price",
        "Kms_Driven",
        "Fuel_Type"
    ]
].isnull().sum())


# ------------------------------------------------------------
# 9. CONVERT NUMERIC COLUMNS TO NUMERIC TYPE
# ------------------------------------------------------------

df["Selling_Price"] = pd.to_numeric(
    df["Selling_Price"],
    errors="coerce"
)

df["Present_Price"] = pd.to_numeric(
    df["Present_Price"],
    errors="coerce"
)

df["Kms_Driven"] = pd.to_numeric(
    df["Kms_Driven"],
    errors="coerce"
)

df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)


# ------------------------------------------------------------
# 10. HANDLE MISSING VALUES
# ------------------------------------------------------------

# Numeric columns → Mean

df["Selling_Price"] = df["Selling_Price"].fillna(
    df["Selling_Price"].mean()
)

df["Present_Price"] = df["Present_Price"].fillna(
    df["Present_Price"].mean()
)

df["Kms_Driven"] = df["Kms_Driven"].fillna(
    df["Kms_Driven"].mean()
)


# Categorical column → Mode

df["Fuel_Type"] = df["Fuel_Type"].fillna(
    df["Fuel_Type"].mode()[0]
)


# ------------------------------------------------------------
# 11. CONVERT SELLING PRICE TO NUMPY ARRAY
# ------------------------------------------------------------

selling_price_array = df["Selling_Price"].to_numpy()


# ------------------------------------------------------------
# 12. CONVERT KMS DRIVEN TO NUMPY ARRAY
# ------------------------------------------------------------

kms_driven_array = df["Kms_Driven"].to_numpy()


# ------------------------------------------------------------
# 13. NUMPY CALCULATIONS
# ------------------------------------------------------------

minimum_selling_price = np.min(selling_price_array)

maximum_selling_price = np.max(selling_price_array)

average_selling_price = np.mean(selling_price_array)


# ------------------------------------------------------------
# 14. DISPLAY RESULTS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("NUMPY CALCULATIONS")
print("=" * 60)

print("\nMinimum Selling Price:",
      minimum_selling_price)

print("Maximum Selling Price:",
      maximum_selling_price)

print("Average Selling Price:",
      average_selling_price)


# ------------------------------------------------------------
# 15. FINAL MISSING VALUE CHECK
# ------------------------------------------------------------

print("\nFINAL MISSING VALUE CHECK:")
print(
    df[
        [
            "Selling_Price",
            "Present_Price",
            "Kms_Driven",
            "Fuel_Type"
        ]
    ].isnull().sum()
)


# ------------------------------------------------------------
# 16. FINAL MESSAGE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SCENARIO 1 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 2
#             Selling Price Trend
#                 Line Graph
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 2: SELLING PRICE TREND")
print("=" * 60)


# ------------------------------------------------------------
# 1. SELECT REQUIRED COLUMNS
# ------------------------------------------------------------

sample = df[["Car_Name", "Selling_Price"]]


# ------------------------------------------------------------
# 2. TAKE FIRST 10 ROWS
# ------------------------------------------------------------

sample = sample.head(10)

print("\nFIRST 10 CARS:")
print(sample)


# ------------------------------------------------------------
# 3. CONVERT SELLING PRICE INTO NUMPY ARRAY
# ------------------------------------------------------------

selling_price_array = sample["Selling_Price"].to_numpy()

print("\nSELLING PRICE NUMPY ARRAY:")
print(selling_price_array)


# ------------------------------------------------------------
# 4. CREATE X-AXIS VALUES
# ------------------------------------------------------------

x_values = np.arange(len(selling_price_array))

print("\nX-AXIS VALUES:")
print(x_values)


# ------------------------------------------------------------
# 5. CREATE LINE GRAPH
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    x_values,
    selling_price_array,
    marker="o"
)


# ------------------------------------------------------------
# 6. ADD TITLE AND LABELS
# ------------------------------------------------------------

plt.title("Selling Price Trend (First 10 Cars)")

plt.xlabel("Row Index")

plt.ylabel("Selling Price")


# ------------------------------------------------------------
# 7. ADD GRID
# ------------------------------------------------------------

plt.grid(True)


# ------------------------------------------------------------
# 8. SAVE GRAPH
# ------------------------------------------------------------

plt.savefig(
    "Graphs/selling_price_line.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 9. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 10. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 2 graph saved successfully.")

print("=" * 60)
print("SCENARIO 2 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 3
#          EXPENSIVE CARS ANALYSIS
#            FILTERING + BAR CHART
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 3: EXPENSIVE CARS ANALYSIS")
print("=" * 60)


# ------------------------------------------------------------
# 1. FILTER EXPENSIVE CARS
# ------------------------------------------------------------

expensive_cars = df[df["Selling_Price"] > 10]

print("\nEXPENSIVE CARS:")
print(expensive_cars)


# ------------------------------------------------------------
# 2. GROUP BY FUEL TYPE AND COUNT CARS
# ------------------------------------------------------------

fuel_counts = expensive_cars.groupby("Fuel_Type").size()

print("\nNUMBER OF EXPENSIVE CARS BY FUEL TYPE:")
print(fuel_counts)


# ------------------------------------------------------------
# 3. CONVERT FUEL TYPE LABELS INTO NUMPY ARRAY
# ------------------------------------------------------------

fuel_labels = np.array(fuel_counts.index)

print("\nFUEL TYPE NUMPY ARRAY:")
print(fuel_labels)


# ------------------------------------------------------------
# 4. CONVERT COUNTS INTO NUMPY ARRAY
# ------------------------------------------------------------

fuel_values = np.array(fuel_counts.values)

print("\nCOUNT NUMPY ARRAY:")
print(fuel_values)


# ------------------------------------------------------------
# 5. CREATE BAR CHART
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    fuel_labels,
    fuel_values
)


# ------------------------------------------------------------
# 6. ADD TITLE
# ------------------------------------------------------------

plt.title("Fuel Types of Expensive Cars")


# ------------------------------------------------------------
# 7. ADD X-AXIS LABEL
# ------------------------------------------------------------

plt.xlabel("Fuel Type")


# ------------------------------------------------------------
# 8. ADD Y-AXIS LABEL
# ------------------------------------------------------------

plt.ylabel("Count of Expensive Cars")


# ------------------------------------------------------------
# 9. SAVE GRAPH
# ------------------------------------------------------------

plt.tight_layout()

plt.savefig(
    "Graphs/expensive_car_analysis.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 10. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 11. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 3 graph saved successfully.")

print("=" * 60)
print("SCENARIO 3 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 4
#            FUEL TYPE DISTRIBUTION
#                  PIE CHART
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 4: FUEL TYPE DISTRIBUTION")
print("=" * 60)


# ------------------------------------------------------------
# 1. COUNT CARS BY FUEL TYPE
# ------------------------------------------------------------

fuel_counts = df["Fuel_Type"].value_counts()

print("\nFUEL TYPE COUNTS:")
print(fuel_counts)


# ------------------------------------------------------------
# 2. PREPARE LABELS
# ------------------------------------------------------------

labels = fuel_counts.index

print("\nFUEL TYPE LABELS:")
print(labels)


# ------------------------------------------------------------
# 3. CONVERT VALUES INTO NUMPY ARRAY
# ------------------------------------------------------------

values = np.array(fuel_counts.values)

print("\nFUEL TYPE VALUES:")
print(values)


# ------------------------------------------------------------
# 4. CREATE PIE CHART
# ------------------------------------------------------------

plt.figure(figsize=(8, 8))

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140
)


# ------------------------------------------------------------
# 5. ADD TITLE
# ------------------------------------------------------------

plt.title("Overall Fuel Type Distribution")


# ------------------------------------------------------------
# 6. SAVE GRAPH
# ------------------------------------------------------------

plt.savefig(
    "Graphs/fuel_type_distribution.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 7. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 8. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 4 graph saved successfully.")

print("=" * 60)
print("SCENARIO 4 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 5
#       PRESENT PRICE VS SELLING PRICE
#                 SCATTER PLOT
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 5: PRESENT PRICE VS SELLING PRICE")
print("=" * 60)


# ------------------------------------------------------------
# 1. SELECT REQUIRED COLUMNS
# ------------------------------------------------------------

price_data = df[["Present_Price", "Selling_Price"]]

print("\nSELECTED PRICE DATA:")
print(price_data.head())


# ------------------------------------------------------------
# 2. REMOVE MISSING VALUES
# ------------------------------------------------------------

price_data = price_data.dropna()

print("\nDATA AFTER REMOVING MISSING VALUES:")
print(price_data.head())


# ------------------------------------------------------------
# 3. TAKE FIRST 100 ROWS
# ------------------------------------------------------------

sample_data = price_data.head(100)

print("\nFIRST 100 ROWS USED FOR ANALYSIS:")
print(sample_data)


# ------------------------------------------------------------
# 4. CONVERT PRESENT PRICE TO NUMPY ARRAY
# ------------------------------------------------------------

present_price_array = sample_data["Present_Price"].to_numpy()

print("\nPRESENT PRICE NUMPY ARRAY:")
print(present_price_array)


# ------------------------------------------------------------
# 5. CONVERT SELLING PRICE TO NUMPY ARRAY
# ------------------------------------------------------------

selling_price_array = sample_data["Selling_Price"].to_numpy()

print("\nSELLING PRICE NUMPY ARRAY:")
print(selling_price_array)


# ------------------------------------------------------------
# 6. CREATE SCATTER PLOT
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    present_price_array,
    selling_price_array,
    alpha=0.7
)


# ------------------------------------------------------------
# 7. ADD TITLE
# ------------------------------------------------------------

plt.title("Relationship: Present Price vs Selling Price")


# ------------------------------------------------------------
# 8. ADD X-AXIS LABEL
# ------------------------------------------------------------

plt.xlabel("Present Price")


# ------------------------------------------------------------
# 9. ADD Y-AXIS LABEL
# ------------------------------------------------------------

plt.ylabel("Selling Price")


# ------------------------------------------------------------
# 10. ADD GRID
# ------------------------------------------------------------

plt.grid(True)


# ------------------------------------------------------------
# 11. SAVE GRAPH
# ------------------------------------------------------------

plt.tight_layout()

plt.savefig(
    "Graphs/present_vs_selling_scatter.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 12. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 13. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 5 graph saved successfully.")

print("=" * 60)
print("SCENARIO 5 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 6
#          CAR AGE CATEGORY ANALYSIS
#                  BAR CHART
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 6: CAR AGE CATEGORY ANALYSIS")
print("=" * 60)


# ------------------------------------------------------------
# 1. CREATE CAR AGE CATEGORY
# ------------------------------------------------------------

df["Car Age Category"] = np.select(
    [
        df["Year"] >= 2015,
        (df["Year"] >= 2010) & (df["Year"] <= 2014),
        df["Year"] < 2010
    ],
    [
        "New",
        "Medium",
        "Old"
    ],
    default="Unknown"
)


# ------------------------------------------------------------
# 2. DISPLAY CAR AGE CATEGORY
# ------------------------------------------------------------

print("\nCAR AGE CATEGORY:")
print(df[["Year", "Car Age Category"]].head(20))


# ------------------------------------------------------------
# 3. COUNT CARS IN EACH CATEGORY
# ------------------------------------------------------------

age_counts = df["Car Age Category"].value_counts()

print("\nNUMBER OF CARS IN EACH AGE CATEGORY:")
print(age_counts)


# ------------------------------------------------------------
# 4. CONVERT CATEGORY NAMES INTO NUMPY ARRAY
# ------------------------------------------------------------

age_labels = np.array(age_counts.index)

print("\nAGE CATEGORY NUMPY ARRAY:")
print(age_labels)


# ------------------------------------------------------------
# 5. CONVERT COUNTS INTO NUMPY ARRAY
# ------------------------------------------------------------

age_values = np.array(age_counts.values)

print("\nAGE COUNT NUMPY ARRAY:")
print(age_values)


# ------------------------------------------------------------
# 6. CREATE BAR CHART
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    age_labels,
    age_values
)


# ------------------------------------------------------------
# 7. ADD TITLE
# ------------------------------------------------------------

plt.title("Car Age Category Distribution")


# ------------------------------------------------------------
# 8. ADD X-AXIS LABEL
# ------------------------------------------------------------

plt.xlabel("Car Age Category")


# ------------------------------------------------------------
# 9. ADD Y-AXIS LABEL
# ------------------------------------------------------------

plt.ylabel("Count of Cars")


# ------------------------------------------------------------
# 10. SAVE GRAPH
# ------------------------------------------------------------

plt.tight_layout()

plt.savefig(
    "Graphs/car_age_category.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 11. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 12. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 6 graph saved successfully.")

print("=" * 60)
print("SCENARIO 6 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 7
#             KMS DRIVEN DISTRIBUTION
#                  HISTOGRAM
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 7: KMS DRIVEN DISTRIBUTION")
print("=" * 60)


# ------------------------------------------------------------
# 1. SELECT KMS_DRIVEN
# ------------------------------------------------------------

kms = df["Kms_Driven"]

print("\nKMS DRIVEN DATA:")
print(kms.head())


# ------------------------------------------------------------
# 2. CONVERT KMS_DRIVEN INTO NUMPY ARRAY
# ------------------------------------------------------------

kms_array = np.array(kms)

print("\nKMS DRIVEN NUMPY ARRAY:")
print(kms_array)


# ------------------------------------------------------------
# 3. CREATE HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    kms_array,
    bins=15
)


# ------------------------------------------------------------
# 4. ADD TITLE
# ------------------------------------------------------------

plt.title("Kms Driven Distribution")


# ------------------------------------------------------------
# 5. ADD X-AXIS LABEL
# ------------------------------------------------------------

plt.xlabel("Kms Driven")


# ------------------------------------------------------------
# 6. ADD Y-AXIS LABEL
# ------------------------------------------------------------

plt.ylabel("Frequency")


# ------------------------------------------------------------
# 7. ADD GRID
# ------------------------------------------------------------

plt.grid(True)


# ------------------------------------------------------------
# 8. SAVE GRAPH
# ------------------------------------------------------------

plt.tight_layout()

plt.savefig(
    "Graphs/kms_driven_histogram.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 9. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 10. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 7 graph saved successfully.")

print("=" * 60)
print("SCENARIO 7 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 8
#       TRANSMISSION-WISE SELLING PRICE
#                 COMPARISON
#                  BAR CHART
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 8: TRANSMISSION-WISE SELLING PRICE")
print("=" * 60)


# ------------------------------------------------------------
# 1. GROUP BY TRANSMISSION AND CALCULATE AVERAGE
# ------------------------------------------------------------

avg_price = df.groupby("Transmission")["Selling_Price"].mean()

print("\nAVERAGE SELLING PRICE BY TRANSMISSION:")
print(avg_price)


# ------------------------------------------------------------
# 2. CONVERT TRANSMISSION LABELS INTO NUMPY ARRAY
# ------------------------------------------------------------

transmission_array = np.array(avg_price.index)

print("\nTRANSMISSION NUMPY ARRAY:")
print(transmission_array)


# ------------------------------------------------------------
# 3. CONVERT AVERAGE PRICES INTO NUMPY ARRAY
# ------------------------------------------------------------

price_array = np.array(avg_price.values)

print("\nAVERAGE PRICE NUMPY ARRAY:")
print(price_array)


# ------------------------------------------------------------
# 4. CREATE BAR CHART
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    transmission_array,
    price_array
)


# ------------------------------------------------------------
# 5. ADD TITLE
# ------------------------------------------------------------

plt.title("Average Selling Price by Transmission")


# ------------------------------------------------------------
# 6. ADD X-AXIS LABEL
# ------------------------------------------------------------

plt.xlabel("Transmission")


# ------------------------------------------------------------
# 7. ADD Y-AXIS LABEL
# ------------------------------------------------------------

plt.ylabel("Average Selling Price")


# ------------------------------------------------------------
# 8. SAVE GRAPH
# ------------------------------------------------------------

plt.tight_layout()

plt.savefig(
    "Graphs/transmission_selling_price.png",
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 9. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()

plt.close()


# ------------------------------------------------------------
# 10. SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 8 graph saved successfully.")

print("=" * 60)
print("SCENARIO 8 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 9
#              SELLER TYPE ANALYSIS
#             BAR CHART + PIE CHART
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 9: SELLER TYPE ANALYSIS")
print("=" * 60)


# ------------------------------------------------------------
# 1. COUNT SELLER TYPES
# ------------------------------------------------------------

seller_counts = df["Seller_Type"].value_counts().sort_values(
    ascending=False
)

print("\nSELLER TYPE COUNTS:")
print(seller_counts)


# ------------------------------------------------------------
# 2. CONVERT SELLER LABELS INTO NUMPY ARRAY
# ------------------------------------------------------------

seller_labels = seller_counts.index.to_numpy()

print("\nSELLER TYPE NUMPY ARRAY:")
print(seller_labels)


# ------------------------------------------------------------
# 3. CONVERT SELLER COUNTS INTO NUMPY ARRAY
# ------------------------------------------------------------

seller_values = seller_counts.values

print("\nSELLER COUNT NUMPY ARRAY:")
print(seller_values)


# ============================================================
#                 BAR CHART
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    seller_labels,
    seller_values
)

plt.title("Seller Type Distribution")
plt.xlabel("Seller Type")
plt.ylabel("Number of Cars")

plt.tight_layout()

plt.savefig(
    "Graphs/seller_type_bar.png",
    bbox_inches="tight"
)

plt.show()

plt.close()


# ============================================================
#                 PIE CHART
# ============================================================

plt.figure(figsize=(7, 7))

plt.pie(
    seller_values,
    labels=seller_labels,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Seller Type Distribution - Pie Chart")

plt.tight_layout()

plt.savefig(
    "Graphs/seller_type_pie.png",
    bbox_inches="tight"
)

plt.show()

plt.close()


# ============================================================
#                 FIND MOST COMMON SELLER
# ============================================================

most_common_seller = seller_counts.idxmax()

print("\nMost Common Seller Type:", most_common_seller)


# ------------------------------------------------------------
# SUCCESS MESSAGE
# ------------------------------------------------------------

print("\nScenario 9 graphs saved successfully.")

print("=" * 60)
print("SCENARIO 9 COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
#                 SCENARIO 10
#        ADVANCED ANALYSIS + MULTIPLE GRAPHS
# ============================================================

print("\n" + "=" * 60)
print("SCENARIO 10: ADVANCED ANALYSIS")
print("=" * 60)


# ============================================================
# PART 1: FEATURE CREATION
# ============================================================

# Create Price Difference column

df["Price_Difference"] = (
    df["Present_Price"] - df["Selling_Price"]
)

print("\nPRICE DIFFERENCE:")
print(
    df[
        ["Present_Price", "Selling_Price", "Price_Difference"]
    ].head()
)


# ============================================================
# PART 2: NUMPY CALCULATIONS
# ============================================================

# Convert Selling_Price into NumPy array

selling_np = df["Selling_Price"].to_numpy()


# Convert Price_Difference into NumPy array

price_diff_np = df["Price_Difference"].to_numpy()


# Calculate price changes between consecutive rows

price_change = np.diff(selling_np)


# Calculate depreciation statistics

avg_depreciation = np.mean(price_diff_np)

max_depreciation = np.max(price_diff_np)

min_depreciation = np.min(price_diff_np)


print("\nDEPRECIATION ANALYSIS:")

print(
    "Average Depreciation:",
    avg_depreciation
)

print(
    "Maximum Depreciation:",
    max_depreciation
)

print(
    "Minimum Depreciation:",
    min_depreciation
)

print(
    "\nNumber of Consecutive Price Changes:",
    len(price_change)
)


# ============================================================
# PART 3 — VISUALIZATION 1
# AVERAGE SELLING PRICE BY YEAR
# ============================================================

year_avg = (
    df.groupby("Year")["Selling_Price"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(10, 5))

plt.plot(
    year_avg.index,
    year_avg.values,
    marker="o"
)

plt.title("Average Selling Price by Year")

plt.xlabel("Year")

plt.ylabel("Average Selling Price")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Graphs/year_trend.png",
    bbox_inches="tight"
)

plt.show()

plt.close()


# ============================================================
# PART 3 — VISUALIZATION 2
# AVERAGE SELLING PRICE BY FUEL TYPE
# ============================================================

fuel_avg = (
    df.groupby("Fuel_Type")["Selling_Price"]
    .mean()
    .sort_values()
)

print("\nAVERAGE SELLING PRICE BY FUEL TYPE:")

print(fuel_avg)


plt.figure(figsize=(8, 5))

plt.bar(
    fuel_avg.index,
    fuel_avg.values
)

plt.title("Average Selling Price by Fuel Type")

plt.xlabel("Fuel Type")

plt.ylabel("Average Selling Price")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    "Graphs/fuel_bar.png",
    bbox_inches="tight"
)

plt.show()

plt.close()


# ============================================================
# PART 3 — VISUALIZATION 3
# AVERAGE SELLING PRICE BY TRANSMISSION
# ============================================================

trans_avg = (
    df.groupby("Transmission")["Selling_Price"]
    .mean()
    .sort_values()
)

print("\nAVERAGE SELLING PRICE BY TRANSMISSION:")

print(trans_avg)


plt.figure(figsize=(8, 5))

plt.bar(
    trans_avg.index,
    trans_avg.values
)

plt.title("Average Selling Price by Transmission")

plt.xlabel("Transmission")

plt.ylabel("Average Selling Price")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    "Graphs/transmission_bar.png",
    bbox_inches="tight"
)

plt.show()

plt.close()


# ============================================================
# PART 3 — VISUALIZATION 4
# SELLING PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    selling_np,
    bins=20
)

plt.title("Selling Price Distribution")

plt.xlabel("Selling Price")

plt.ylabel("Frequency")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    "Graphs/selling_price_histogram.png",
    bbox_inches="tight"
)

plt.show()

plt.close()


# ============================================================
# PART 4 — BUSINESS INSIGHTS
# ============================================================

# ------------------------------------------------------------
# INSIGHT 1: FUEL TYPE WITH HIGHEST AVERAGE SELLING PRICE
# ------------------------------------------------------------

highest_fuel = fuel_avg.idxmax()

highest_fuel_price = fuel_avg.max()

print(
    "\n1. Fuel type with highest average selling price:",
    highest_fuel
)

print(
    "Average selling price:",
    highest_fuel_price
)


# ------------------------------------------------------------
# INSIGHT 2: TRANSMISSION WITH HIGHER AVERAGE SELLING PRICE
# ------------------------------------------------------------

higher_transmission = trans_avg.idxmax()

higher_transmission_price = trans_avg.max()

print(
    "\n2. Transmission with higher average selling price:",
    higher_transmission
)

print(
    "Average selling price:",
    higher_transmission_price
)


# ------------------------------------------------------------
# INSIGHT 3: LOWER OR HIGHER SELLING PRICES
# ------------------------------------------------------------

median_selling_price = df["Selling_Price"].median()

lower_price_count = (
    df["Selling_Price"] < median_selling_price
).sum()

higher_price_count = (
    df["Selling_Price"] >= median_selling_price
).sum()

print(
    "\n3. Selling price concentration:"
)

print(
    "Median selling price:",
    median_selling_price
)

print(
    "Cars below median:",
    lower_price_count
)

print(
    "Cars at or above median:",
    higher_price_count
)


if lower_price_count > higher_price_count:

    print(
        "Most cars are concentrated in lower selling prices."
    )

else:

    print(
        "Most cars are concentrated in higher selling prices."
    )


# ------------------------------------------------------------
# INSIGHT 4: OLDER CARS AND SELLING PRICE
# ------------------------------------------------------------

old_cars = df[df["Year"] < 2010]

new_cars = df[df["Year"] >= 2015]

old_average_price = old_cars["Selling_Price"].mean()

new_average_price = new_cars["Selling_Price"].mean()

print(
    "\n4. Older cars vs newer cars:"
)

print(
    "Average selling price of old cars:",
    old_average_price
)

print(
    "Average selling price of new cars:",
    new_average_price
)


if old_average_price < new_average_price:

    print(
        "Older cars tend to have lower selling prices."
    )

else:

    print(
        "Older cars do not tend to have lower selling prices "
        "in this dataset."
    )


# ============================================================
# FINAL SUCCESS MESSAGE
# ============================================================

print("\n" + "=" * 60)

print(
    "SCENARIO 10 COMPLETED SUCCESSFULLY"
)

print("=" * 60)