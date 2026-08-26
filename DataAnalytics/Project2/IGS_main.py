
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create graphs folder if it doesn't exist
os.makedirs("graphs", exist_ok=True)


# SCENARIO 1: Data Loading & Preprocessing

print("=" * 60)
print("SCENARIO 1: Data Loading & Preprocessing")
print("=" * 60)

df = pd.read_csv("ign.csv")

# Display first 5 and last 5 rows
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape of dataset:", df.shape)

# Remove unnecessary index column
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])
    print("\nDropped 'Unnamed: 0' column.")

# Check missing values in key columns
print("\nMissing values in score, genre, platform:")
print(df[["score", "genre", "platform"]].isnull().sum())

# Handle missing values
df["score"] = df["score"].fillna(df["score"].mean())
df["genre"] = df["genre"].fillna(df["genre"].mode()[0])

# Ensure correct data types
df["score"] = df["score"].astype(float)
df["release_year"] = df["release_year"].astype(int)
df["release_month"] = df["release_month"].astype(int)
df["release_day"] = df["release_day"].astype(int)

print("\nData types after conversion:")
print(df[["score", "release_year", "release_month", "release_day"]].dtypes)


# SCENARIO 2: Line Graph (Score Trend) + Save

print("\n" + "=" * 60)
print("SCENARIO 2: Line Graph - Score Trend Over Years")
print("=" * 60)

yearly_avg_score = df.groupby("release_year")["score"].mean()

years = np.array(yearly_avg_score.index)
avg_scores = np.array(yearly_avg_score.values)

plt.figure(figsize=(10, 6))
plt.plot(years, avg_scores, marker="o", color="steelblue")
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/avg_score_trend.png")
plt.close()
print("Saved: graphs/avg_score_trend.png")


# SCENARIO 3: Filtering + Bar Chart + Save

print("\n" + "=" * 60)
print("SCENARIO 3: Top Platforms (score > 7)")
print("=" * 60)

high_rated = df[df["score"] > 7]
platform_counts = high_rated["platform"].value_counts().head(10)

platforms = np.array(platform_counts.index)
counts = np.array(platform_counts.values)

plt.figure(figsize=(10, 6))
plt.bar(platforms, counts, color="seagreen")
plt.title("Top 10 Platforms by Count of High-Rated Games (score > 7)")
plt.xlabel("Platform")
plt.ylabel("Count of Games")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("graphs/top_platforms_bar.png")
plt.close()
print("Saved: graphs/top_platforms_bar.png")


# SCENARIO 4: Aggregation + Pie Chart + Save

print("\n" + "=" * 60)
print("SCENARIO 4: Genre Distribution (Top 5)")
print("=" * 60)

genre_counts = df["genre"].value_counts().head(5)

labels = genre_counts.index
values = genre_counts.values

plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90,
        colors=plt.cm.Pastel1.colors)
plt.title("Top 5 Genre Distribution")
plt.tight_layout()
plt.savefig("graphs/genre_distribution.png")
plt.close()
print("Saved: graphs/genre_distribution.png")

# SCENARIO 5: Advanced Analysis + Multiple Graphs
print("\n" + "=" * 60)
print("SCENARIO 5: Advanced Analysis")
print("=" * 60)

# --- Part 1: Feature Engineering ---
def categorize_score(score):
    if score >= 9:
        return "Excellent"
    elif score >= 7:
        return "Good"
    else:
        return "Average"

df["score_category"] = df["score"].apply(categorize_score)

df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0})

print("\nscore_category value counts:")
print(df["score_category"].value_counts())

# --- Part 2: NumPy Analysis ---
yearly_avg_score = df.groupby("release_year")["score"].mean()
yearly_scores_np = np.array(yearly_avg_score.values)
yearly_growth = np.diff(yearly_scores_np)

print("\nYearly score growth (np.diff):")
for yr, growth in zip(yearly_avg_score.index[1:], yearly_growth):
    print(f"  {yr}: {growth:+.3f}")

# --- Part 3: Visualizations ---

# 3a. Line Graph - Average score per release_year
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg_score.index, yearly_avg_score.values,
         marker="o", color="darkorange")
plt.title("Average Score Trend by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/score_trend.png")
plt.close()
print("\nSaved: graphs/score_trend.png")

# 3b. Stacked Bar Chart - score_category counts per release_year
category_by_year = pd.crosstab(df["release_year"], df["score_category"])

plt.figure(figsize=(12, 7))
category_by_year.plot(kind="bar", stacked=True, ax=plt.gca(),
                       colormap="viridis")
plt.title("Score Category Distribution by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Count of Games")
plt.legend(title="Score Category")
plt.tight_layout()
plt.savefig("graphs/score_category_stacked.png")
plt.close()
print("Saved: graphs/score_category_stacked.png")

# 3c. Histogram - distribution of score
plt.figure(figsize=(10, 6))
plt.hist(df["score"], bins=20, color="mediumpurple", edgecolor="black")
plt.title("Distribution of Game Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("graphs/score_distribution.png")
plt.close()
print("Saved: graphs/score_distribution.png")

# --- Part 5: Insights ---
print("\n" + "-" * 60)
print("INSIGHTS")
print("-" * 60)

best_year = yearly_avg_score.idxmax()
best_score = yearly_avg_score.max()
print(f"1. Year with highest average score: {best_year} (avg score: {best_score:.2f})")

trend_direction = "increased" if yearly_growth[-1] > 0 else "decreased"
overall_trend = "increased" if yearly_avg_score.iloc[-1] > yearly_avg_score.iloc[0] else "decreased"
print(f"2. Overall, average scores have {overall_trend} from "
      f"{yearly_avg_score.index[0]} to {yearly_avg_score.index[-1]}.")

if "editors_choice" in df.columns:
    corr = df["editors_choice"].corr(df["score"])
    print(f"3. Correlation between editors_choice and score: {corr:.3f}")
    if corr > 0.3:
        print("   -> Editors' Choice games tend to have notably higher scores.")
    elif corr > 0:
        print("   -> Slight positive relationship between editors_choice and score.")
    else:
        print("   -> No meaningful relationship found.")

print("\nAll tasks completed. Graphs saved in the 'graphs' folder.")
