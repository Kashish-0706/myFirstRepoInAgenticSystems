import pandas as pd
import numpy as np

# creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finanace", 
        "HR", "Finanace", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract", "Pending docs", "Verified",
        "Intern", "New joiner", "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
print(df)

# counting total null values in each column
null_vals = df.isnull().sum()
print("Total null values in each column:\n", null_vals)

# filling null values of "salary" column with "salary mean"
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print("Null values of 'Salary' column filled with 'Salary mean':\n", df)

# dropping unnecessary column "Temporary_Notes"
df_clean = df.drop(columns = ["Temporary_Notes"])
print("Removing unnecessary column 'Temporary_Notes':\n ", df_clean)

# renaming "Salary" column to "Annual_Salary"
df = df.rename(columns = {"Salary": "Annual_Salary"})
print("Renaming 'Salary' column to 'Annual_Salary':\n", df)

# groupby "Department" to compute "Salary mean" and "Employee count"
summary_table = df.groupby("Department")["Annual_Salary"].agg(["mean","count"])
print(summary_table)
      