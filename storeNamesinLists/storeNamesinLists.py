personName=[]

while True:
    print("Whats the name of the person, if no name then leave blank")
    name=str(input())
    if name=="":
        break
    personName= personName + [name]

for names in personName:
     print(names)
