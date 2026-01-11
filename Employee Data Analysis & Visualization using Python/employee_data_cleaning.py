from itertools import groupby

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df=pd.read_excel("employee_random_data_with_nan_duplicates.xlsx")



#filling null values 

df["Name"].fillna("N/A",inplace=True)

# calculate an average age to replace the missing age value
df["Age"].fillna(df["Age"].mean(),inplace =True)
      
#replace the city name to unknown
df["City"].fillna("N/A",inplace=True)

#replace Department name to unknown
df["Department"].fillna("N/A",inplace=True)

# calculate an average salary to replace the missing salary value
df["Salary"].fillna(df["Salary"].mean(),inplace=True)

#replace performance to unknown
df["Performance"].fillna("N/A",inplace=True)


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


#matplotlib
figure,axes=plt.subplots(2,2)

#first chart employees count per department
axes[0,0].pie(count.values,
              labels=count.index,
              autopct="%1.1f%%")

axes[0,0].set_title("Employee per Department",fontweight="bold")


#second chart average salary per department
avg_dep_sal=df.groupby("Department")["Salary"].mean()

axes[0,1].barh(avg_dep_sal.index,avg_dep_sal.values)
axes[0,1].set_title("Avg Employee salary",fontweight="bold")
axes[0,1].set_xlabel("Salary",fontweight="bold")
axes[0,1].set_ylabel("Department",fontweight="bold")
axes[0,1].set_xlim(0,80000)
axes[0,1].set_xticks([0,20000,40000,60000,80000])
axes[0,1].set_xticklabels([0,"20k","40k","60k","80k"])
# axes[0,1].tick_params(axis="x",labelrotation=45)

#third chart employees per city

axes[1,0].barh(epc.index,epc.values)
axes[1,0].set_title("Employee per city",fontweight="bold")
axes[1,0].set_xlabel("Count",fontweight="bold")
axes[1,0].set_ylabel("City",fontweight="bold")
axes[1,0].set_xlim(0,20)


#fourth chart salary distribution
axes[1,1].hist(df["Salary"],bins=10)
axes[1,1].set_title("Salary Distribution",fontweight="bold")
axes[1,1].set_xlabel("Salary",fontweight="bold")
axes[1,1].set_ylabel("Count",fontweight="bold")
axes[1,1].set_xlim(0,120000)
axes[1,1].set_ylim(0,15)
axes[1,1].set_xticks([0,40000,80000,120000])

plt.tight_layout()
plt.show()

#save as excel 
df.to_excel("clean_data.xlsx",index=False)

