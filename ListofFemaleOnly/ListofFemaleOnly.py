#from given list of lists, give list of only female patients

patients = [ ['Milos', 'Jones', 48, 'male', 'smoker', 210], 
             ['Delia', 'Chan', 39, 'female', 'non-smoker', 170], 
             ['Denise', 'Ross', 62, 'female', 'non-smoker', 150] ]

femaleList=[]

for values in patients:
    if values[3] == 'female':
        femaleList.append(values[0:2])    #prints first and last name 
print(femaleList)

#print("All the females in the list are the following,")
#print ('\n') .join(map(str,femaleList))

