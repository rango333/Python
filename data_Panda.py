# ### Output one DataFrame in its regular format along with its type and two other DataFrames merged

# If pandas not install, do so by typing: pip install pandas

# ## Create and output a DataFrame from your own dictionary of lists for practice

import pandas as pd

# Create a dictionary of lists
data = {"A": [-1, 0, 1, 2, 3], "B": [4, 5, 6, 7, 8], "C": [7, 8, 9, 10, 11]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)




# ## Merge two DataFrames

# create two DataFrames
df1 = pd.DataFrame({"key": ["K0", "K1", "K2", "K35"],
                    "A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "X2", "B3"]})

df2 = pd.DataFrame({"key": ["K0", "K1", "K2", "K3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]})

# merge the two DataFrames using the "key" column as the common column
pd.merge(df1, df2, on="key", how="inner")

pd.merge(df1, df2, on="key", how="outer")

# Print the regular format DataFrame type
print(type(df))

# Print the DataFrame in regular format
print(df)

# Print the the two merged DataFrames
print("\n", df1)
print("\n", df2)

# Output   <class 'pandas.core.frame.DataFrame'>
#             A  B   C
#          0 -1  4   7
#          1  0  5   8
#          2  1  6   9
#          3  2  7  10
#          4  3  8  11
#
#              key   A   B
#          0   K0  A0  B0
#          1   K1  A1  B1
#          2   K2  A2  X2
#          3  K35  A3  B3
#
#             key   C   D
#          0  K0  C0  D0
#          1  K1  C1  D1
#          2  K2  C2  D2
#          3  K3  C3  D3