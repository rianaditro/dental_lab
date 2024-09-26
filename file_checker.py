import pandas as pd
import numpy as np


df = pd.read_excel("clean_data.xlsx", index_col=0)
print(len(df))

# remove duplicate
df = df.drop_duplicates(subset=["nama", "no. telp"], keep="first")
# remove empty
df = df.dropna(how='all').replace('', np.nan).dropna(how='all')

# reformat no. telp
to_remove = {
    "-": "",
    "\(": "",
    "\)": "",
    " ": ""
}

df["no. telp"] = df["no. telp"].replace(to_remove, regex=True)

# remove valid column
df = df.drop(columns=["valid"])

print(len(df))

# save to excel
df = df.reset_index(drop=True)
df.index = df.index + 1

df.to_excel("dental3.xlsx", index_label="index")

print(df.info())