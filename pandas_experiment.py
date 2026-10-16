import pandas as pd

df = pd.read_csv('data.csv')
# print(df.to_string)

#  Printing top 10 
top_10 =df.head(2)
bottom_10 =df.tail(10)
# print(top_10)
# print(bottom_10)
print(df.info())
# pd.options.display.max_rows =10000
# print(pd.options.display.max_rows) 

json_read =pd.read_json('data_json.json')
# print(json_read.to_string())