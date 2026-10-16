import pandas as pd

df = pd.read_csv('data.csv')

# Empty cells
new_df = df.dropna()

new_df_null = df.dropna(inplace=True)

df.fillna({"Calories": 130}, inplace=True)

x = df["Calories"].mean()

print('Mean_value',x)

df.fillna({"Calories": x}, inplace=True)

y = df["Calories"].median()

print('Median_value',y)

df.fillna({"Calories": y}, inplace=True)


z = df["Calories"].mode()

print('Mode_value',z)

df.fillna({"Calories": z}, inplace=True)

# Bad data could be:

import pandas as pd

df_sample = pd.read_csv('sample.csv')

df_sample['Date'] = pd.to_datetime(df_sample['Date'], format='mixed')

print(df_sample.to_string())


# Data in wrong format
# Wrong data
df_sample.loc[7, 'Duration'] = 45
print(df_sample)

df_sample.loc[df_sample["Duration"] > 120, "Duration"] = 120

df = df[df["Duration"] <= 120]
# Duplicates

df.drop_duplicates(inplace = True)
