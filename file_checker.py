import pandas as pd


df = pd.read_excel("dental.xlsx")

print(df["valid"].value_counts())

print(df.isnull().sum())