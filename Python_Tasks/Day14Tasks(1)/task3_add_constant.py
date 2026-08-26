#3. Add Constant to Series (NumPy Operation on Pandas) A Series:
#S = pd.Series([5, 10, 15])
#Task:
# ● Add 5 to each element using NumPy-style operation
# ● Print updated Series

import pandas as pd

S = pd.Series([5, 10, 15])

S = S + 5

print(S)