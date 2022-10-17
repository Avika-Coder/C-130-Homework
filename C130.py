import csv 
import pandas as pd

df=pd.read_csv("final-Hw.csv")
print(len(df))
print(df.shape)

del df['Luminosity']
del df['Distance']
del df['Mass']
del df['Radius']

print(df.shape)
df=df.to_csv("final1-hw.csv")