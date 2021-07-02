list1=["name","designation","age","salary"]
list2=["neelam","programer","24","2400"]
a={}
b={}
c={}
d={}
dict={}
for i in range(len(list1)):
    a[list1[i]]=list2[i]
dict["employee1"]=a


list1=["name","designation","age","salary"]
list3=["komal","trainer","24","20000"]
for i in range(len(list1)):
    b[list1[i]]=list3[i]
dict["employee2"]=b

list1=["name","designation","age","salary"]
list4=["anuradha","HR","25","40000"]
for i in range(len(list1)):
    c[list1[i]]=list4[i]
dict["employee3"]=c


list1=["name","designation","age","salary"]
list5=["Abhishek","manager","29","63000"]
for i in range(len(list1)):
    d[list1[i]]=list3[i]
dict["employee4"]=d

import json

file=open("my file.json","w")
json.dump(dict,file,indent=10)
file.close()



