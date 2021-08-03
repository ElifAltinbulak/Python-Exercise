students=["Ayşe Varlar",
          "Deniz Kuzu",
          "Serkan Uslu",
          "Adnan Portakal",
          "Ceylan Kum"]
ds={}
ll=[]
for i in range(5):
    print("***Course Grade Application***")
    ch=int(input("1-Ayşe Varlar\n2-Deniz Kuzu\n3-Serkan Uslu\n4-Adnan Portakal\n5-Ceylan Kum\n**Please select a number:"))
    print(f"Welcome {students[ch-1]}")
    m=int(float(input("Enter the Midterm Exam: ")))
    p=int(float(input("Enter the Project: ")))
    f=int(float(input("Enter the Final Exam: ")))
    passingGrade=(m*(0.3)+p*(0.3)+f*(0.4))
    ds[students[ch-1]]=passingGrade
for s in ds:
    ll.append(ds[s])
print(f"Student dict:{ds}")
print(f"Student list:{ll}")
ll.sort()
print(ll[::-1])
