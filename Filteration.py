import pandas as pd
data={
    "Name":["aman","riya","karan","neha"],
    "Class":[10,9,10,8],
    "Marks":[85,62,45,78],
}
df=pd.DataFrame(data)
print(df[df["Marks"]>60])
print(df[df["Class"]==10])
print(df[df["Marks"]<70])
print(df[df["Marks"]>75])
print(df[df["Class"]==9])
#names of the student who scored more than 60
print(df[df["Marks"]>60],["Name"])
#name of students who are in class 10th
print(df[df["Class"]==10],["Names"])
# marks of students who scored more than 70
print(df[df["Marks"]>70],["Marks"])

#now loc (location by condition)
#Names and Marks of students who scored more than 70
print(df.loc[df["Marks"]>70],["Names","Marks"])
print(df.loc[(df["Class"]==10)&(df["Marks"]>70),["Name","Marks"]])
print(df.loc[(df["Class"]==10)|(df["Marks"]>80),["Name"]])

#new concept: groupby()
#(REAL WORLD,POWERFUL)
print(df.groupby("Class")["Marks"].mean())
print(df.groupby("Class")["Marks"].max())
print(df.groupby("Name")["Marks"].sum())
print(df.groupby("Name")["Marks"].count())
print(df.groupby("Class")["Marks"].agg(["mean","max","min","count"]))#you can use all in one line also Advanced+Easy 