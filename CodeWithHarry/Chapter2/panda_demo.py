import pandas as pd 
csv_path = "student.txt"
df = pd.read_csv(csv_path)
df.head() # first 5 rows
x = df[['Gender']] # perticular coloumn
print(df.head())
y = df.iloc[0,0] # position based
print("-----------------------------------------")
print(x)
print("----------------------------------------------")
print(y)
print("-------------------------------------")
print(df.loc[0, 'Class'])  # Label-based
