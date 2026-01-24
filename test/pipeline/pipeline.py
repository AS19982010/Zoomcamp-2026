import sys
import pandas as pd 
print("arguments", sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"day": [1, 2], "number_passenger": [3, 4]})
df['month']=month
df.to_parquet(f"output_day_{sys.argv[1]}.parquet") 
print(df.head())
print(df2.head()) 
print(f"Running pipeline for month {month}")
 