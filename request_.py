import requests
import json

req=requests.get(' http://saral.navgurukul.org/api/courses')
a=(req.json())
with open("courses.json","w") as f:
    aa=json.dump(a,f,indent=4)
with open("courses.json","r") as f1:
    r=json.load(f1)
    # print((r))
store=(a["availableCourses"])
i=1
name=[]
id=[]
for i in range(len(store)):
    print(i,store[i]["name"], end="--")
    print(store[i]["id"])
    name.append(store[i]["name"])
    id.append(store[i]["id"])
print(" ")
user=int(input("enter the number.... "))
user1=id[user]
print(user1)
var=requests.get("http://saral.navgurukul.org/api/courses/"+user1+"/exercises")
print(var)
data2=var.json()
slug=[]
count=1
for sec in data2["data"]:
    print(count,sec["name"])
    slug.append(sec["slug"])
    count+=1
    for child in sec["childExercises"]:
        print("      ",count,child["name"])
        slug.append(child["slug"])
        count+=1

var2=int(input("show content slug = "))
var3=requests.get("https://saral.navgurukul.org/api/courses/"+user1+"/exercise/getBySlug?slug="+str(slug[var2-1]))
data3=var3.json()
print(data3["content"])
while True:
    x=var2
    print("....................")
    options=input("enter your option back,next,exit = ")
    if options=="next":
        x+=1
        req=requests.get("https://saral.navgurukul.org/api/courses/"+user1+"/exercise/getBySlug?slug="+str(slug[x-1]))
        r1=req.json()
        print("content",r1["content"])
        print(x)
        break
    elif options=="back":
        c=1
        for dic1 in data2["data"]:
            print(c,dic1["name"])
            c+=1
            for i in dic1["childExercises"]:
                print("    ",c,i["name"])
                c+=1
                break
    else:
        break























