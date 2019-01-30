#key value pairs used in dict
#dict methods -> get, setdefault, keys and values and items

database={'james':'August 19', 'Meri':'Sept 17', 'Vipin':'July 25' }

while True:
    print('Enter the name of person you wish to know bday for')
    name=input()
    if name in database:
        print("The birthday of " + name + "is on " + database[name]) #retrieve name passed by user
        break
    else:
        print("Sorry the person does not exist in the database, what is their bday?")
        birthday=input()
        database[name]=birthday  #assign value to the missing name asked by user
        print("Thank you, the user info has been added.")
