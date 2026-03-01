import pandas as pd

df = pd.read_csv(r'C:\Users\kashi\Documents\Module 1\myFirstRepoInAgenticSystems\python-pandas2-assignment\result.csv')
print("---Selecting single column(Name)---")
students = df['Name'].copy()
print(students)
print("---Selecting multiple columns---")
new_df = df[['Score','Passed','Category']].copy()
print(new_df)
print("---Retrieving first three rows---")
first_3 = df.iloc[:3]
print(first_3)
print("---Retrieving rows with index 'Name'---")
df_indexed = df.set_index('Name')
print(df_indexed.loc[['Kashyap','Ishita','Lavi','Vikas','Anshu']])
print("---Students obtained scores > 85---")
high_scores = df[df['Score']>85]
print(high_scores)
print("---High performing students---")
passed_high = df[(df['Score']>85)&(df['Passed']== True)]
print(passed_high)
print("---Top rankers--")
sorted_df = passed_high.sort_values('Score', ascending=False)
print(sorted_df)