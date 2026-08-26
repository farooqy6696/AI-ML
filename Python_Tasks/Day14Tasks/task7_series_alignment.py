#7. Data Alignment Issue in Series Addition Two Series:
#S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
#S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
#Task:
# ● Add both Series
# ● Explain why some values become NaN
# ● Replace NaN with 0 and compute final result

import pandas as pd

S1 = pd.Series(
    [10, 20, 30],
    index=["a", "b", "c"]
)

S2 = pd.Series(
    [5, 15, 25],
    index=["b", "c", "d"]
)

print("Series 1:")
print(S1)

print("\nSeries 2:")
print(S2)

result = S1 + S2

print("\nAfter adding Series:")
print(result)

result = result.fillna(0)

print("\nAfter replacing NaN with 0:")
print(result)

final_total = result.sum()

print("\nFinal total:")
print(final_total)