import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_excel("student_result_data_dirty.xlsx",index_col="Student_ID")


#placing None where Name and Class are missing 
df[["Name","Class"]]= df[["Name","Class"]].fillna({"Name" : "None",
                            "Class" : "None"})




num_col=["Attendance_Percentage","Maths","Science","English","Social_Studies","Computer"]

# setting range of the columns in num_cols between 0 to 100
df[num_col]=df[num_col].clip(lower=0,upper=100)

#replacing null values with zero 
df[num_col]=df[num_col].fillna(0)

#removing duplicates
df.drop_duplicates(inplace=True)

subject=["Maths","Science","English","Social_Studies","Computer"]

#new columns as total marks
df["Total_Marks"]=df[subject].sum(axis=1)




#Grading conditions
condition=[df["Total_Marks"]>400,
           df["Total_Marks"]>300,
            df["Total_Marks"]>200,
            df["Total_Marks"]>100]

grade=["A","B","C","D"]

#creating grading column
df["Grade"]=np.select(condition,grade,default="Fail")



#top three students 
df.sort_values(by="Total_Marks",ascending=False,inplace=True)
print(df[["Name","Class"]].head(3))



#creating sub graphs
figure,axes=plt.subplots(2,2)

#first chart
axes[0,0].pie(df["Grade"].value_counts(),
            labels=grade,
            autopct="%1.1f%%",
            explode=[0,0.2,0.2,0.2])

axes[0,0].set_title("Grade Distribution",fontweight="bold")


#second chart
avg=df[subject].mean()

axes[0,1].bar(subject,avg)
axes[0,1].set_title("Average Marks per subject",fontweight="bold")
axes[0,1].set_xlabel("Subject",fontweight="bold")
axes[0,1].set_ylabel("Average",fontweight="bold")
axes[0,1].set_ylim(0,100)
axes[0,1].tick_params(axis="x",rotation=30)

#third chart
axes[1,0].scatter(df["Attendance_Percentage"],df["Total_Marks"])
axes[1,0].set_ylim(0,500)
axes[1,0].set_title("Attendance vs Total_marks",fontweight="bold")
axes[1,0].set_xlabel("Attendance",fontweight="bold")
axes[1,0].set_ylabel("Percentage",fontweight="bold")

#fourth chart
top5=df.head()
axes[1,1].bar(top5["Name"],top5["Total_Marks"])
axes[1,1].set_title("Top 5 students",fontweight="bold")
axes[1,1].set_xlabel("Student name",fontweight="bold")
axes[1,1].set_ylabel("Total Marks",fontweight="bold")
axes[1,1].set_ylim(0,500)


plt.tight_layout()
plt.show()

#saving
df.to_excel("Cleaned_Student_Data.xlsx")




