import pandas as pd
import numpy as np



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


df.to_excel("Cleaned_Student_Data.xlsx")

