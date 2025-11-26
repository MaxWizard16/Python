import pandas as pd

# Q1

print(“Pandas Version:”, pd.__version__)

data = {‘Name’: [‘Alice’, ‘Bob’, ‘Charlie’], ‘Age’: [25, 30, 35],
‘City’: [‘New York’, ‘Los Angeles’, ‘Chicago’]} df = pd.DataFrame(data)
print(df)

# Q2

S1 = pd.Series([100,200,300,400,500]) print(S1) print(S1.iloc[1],
S1.iloc[3])

S2 = pd.Series([10,20,30,40,50]) print(S1 + S2)

# Q3

print(df[[‘Name’,‘City’]]) df[‘Salary’] = [50000,60000,70000] print(df)
print(“Average Age:”, df[‘Age’].mean()) print(“Total Salary:”,
df[‘Salary’].sum())

# Q4

print(df[df[‘Age’]>28]) df2 = df.set_index(‘Name’) print(df2)
print(df2.reset_index())

# Q5

emp = pd.DataFrame({‘Name’:[‘John’,‘Jane’,‘Emily’],
‘Department’:[‘Sales’,‘Marketing’,‘HR’], ‘Salary’:[50000,60000,55000]})
print(emp) filtered = emp[emp[‘Salary’]>55000]
print(filtered[[‘Name’,‘Department’]])

# Q6

print(emp.groupby(‘Department’)[‘Salary’].mean())
print(emp.groupby(‘Department’)[‘Salary’].agg([‘min’,‘max’]))

# Q7

df1 = pd.DataFrame({‘Name’:[‘John’,‘Jane’,‘Emily’],
‘Department’:[‘Sales’,‘Marketing’,‘HR’]}) df2 =
pd.DataFrame({‘Name’:[‘John’,‘Jane’,‘Emily’], ‘Experience
(Years)’:[5,7,3]}) merged = pd.merge(df1,df2,on=‘Name’) print(merged)

# Q8

print(merged.sort_values(‘Experience (Years)’, ascending=False))
