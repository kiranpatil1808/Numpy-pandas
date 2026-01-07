import pandas as pd
import numpy as np



df=pd.read_excel("employee_random_data_with_nan_duplicates.xlsx")



#filling null values 

df["Name"].fillna("Unknown",inplace=True)

# calculate an average age to replace the missing age value
df["Age"].fillna(df["Age"].mean(),inplace =True)
      
#replace the city name to unknown
df["City"].fillna("Unknown",inplace=True)

#replace Department name to unknown
df["Department"].fillna("Unknown",inplace=True)

# calculate an average salary to replace the missing salary value
df["Salary"].fillna(df["Salary"].mean(),inplace=True)

#replace performance to unknown
df["Performance"].fillna("Unknown",inplace=True)


#removing duplicates 
df.drop_duplicates(inplace=True)



#calculating avg,min,max and salary average per dept 

avg_salary=df["Salary"].mean()
print("\n Average salary : ", avg_salary)

min_salary=df["Salary"].min()
print("\n minimum salary :", min_salary)

max_salary=df["Salary"].max()
print("\n Maximum salary :",max_salary)


#employee count per department
count=df["Department"].value_counts()
print("\n Employees Number As per Department : \n",count)

#Department wise whole salary of employess
sal=df.groupby("Department")["Salary"].mean()
print("\n Average salary of employees as per Department :\n",sal)


#employees per city
epc=df["City"].value_counts()
print("\n employees number as per city : \n",epc)


#top 5 earners 
top_earners=df.sort_values(by="Salary",ascending=False).head(5)
print("Top 5 earners in organization : \n",top_earners)


#save as excel 
df.to_excel("clean_data.xlsx",index=False)

