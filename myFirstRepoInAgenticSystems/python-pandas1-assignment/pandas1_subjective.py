import pandas as pd

df = pd.read_csv(r'C:\Users\kashi\Documents\Module 1\myFirstRepoInAgenticSystems\python-pandas1-assignment\employees.csv')
print("---First 5 rows---")
print(df.head())
print("---Last 5 rows---")
print(df.tail())
print("---Structural Information---")
print(df.info())
print("---Statistical Summary---")
print(df.describe())
print("---Selecting single column(score)---")
score_column = df['Score']
print(score_column)
print("---Selecting Multiple Columns(Age and Lable)---")
subset_df = df[['Age','Lable']]
print(subset_df)
print("---Filtering rows(Score>80)---")
filtered_df = df[df['Score']>80]
print(filtered_df)
print("---Pipeline execution completed---")