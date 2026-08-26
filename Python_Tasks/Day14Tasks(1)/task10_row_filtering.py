#10. Row Filtering + Aggregation A dataset:
#arr = np.array([
#[100, 200],
#[150, 250],
#[80, 120],
#[300, 400]
#])
#Task:
# ● Convert to DataFrame with columns "Sales", "Profit"
# ● Filter rows where Sales > 100
# ● Find average Profit of filtered rows

import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

df = pd.DataFrame(arr, columns=["Sales", "Profit"])

print("Original DataFrame:")
print(df)

filtered = df[df["Sales"] > 100]

print("\nFiltered rows:")
print(filtered)

average_profit = filtered["Profit"].mean()

print("\nAverage Profit:", average_profit)