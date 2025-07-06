import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("byjus_students.csv")
print(df)

# Average score per subject  
print(df.info())
Average_Scrore = df.groupby("Subject")["Score"].mean().sort_values()
print(Average_Scrore)

# Most active students (TimeSpent)  

Most_Actice = df["TimeSpent"].sort_values(ascending=False).head(5)
print(Most_Actice)

print(df.describe())   

# Strip column names (extra spaces)
df.columns = df.columns.str.strip()

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

print(df.info())


# Standardize city and course type text
df["City"] = df["City"].str.title().str.strip()
df["CourseType"] = df["CourseType"].str.title().str.strip()

# Convert JoinDate to datetime
df["JoinDate"] = pd.to_datetime(df["JoinDate"])

# Final check
print(df.info())

#  Average score per subject           
avg_score = df.groupby("Subject")["Score"].mean()   
print(avg_score)                                              
#  Most active students                
most_actice = df.sort_values(by="TimeSpent", ascending=False).head(5) 
print(most_actice)                                   
# |Performance by city  
city =df.groupby("City")["Score"].mean()    
print(city)                                                 
#  Who scores better: Free or Premium? 

better = df.groupby("CourseType")["Score"].mean()     
print(better)                                            
#  Monthly new student trend           
df["Month"] = df["JoinDate"].dt.to_period("M")
df["Month"].value_counts().sort_index()


df["CourseType"].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()

df.groupby("Subject")["Score"].mean().plot(kind="bar")
plt.show()

df["Month"].value_counts().sort_index().plot(kind="line", marker="o")
plt.show()

sns.boxplot(y=df["Score"])
plt.show()


# Grade column based on Score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Score"].apply(get_grade)


df.to_csv("byjus_cleaned.csv", index=False)
