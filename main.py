import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  "Year":[2020,2010,2026]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
print(myvar.loc[2])
filtered_row =myvar.loc[[1,2]]
print(filtered_row)

# print(myvar)

a =[1,2,3]

series =pd.Series(a)
# print(series)

