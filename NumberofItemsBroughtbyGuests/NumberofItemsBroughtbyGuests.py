#Dictionary -> use of items and get method 

#Total items brought to a party by all guests

guestInfo={'Meri':{'Oranges':5, 'Pickles':2, 'Chips':1},
            'Lara':{'Chips':2, 'Pickles':5, 'Vodka':1}}

#function for finding totalcount of an item from the dictionary
def totalItems(guests,itemName):
    counter=0
    #items method gives key value pairs for dictionary 
    for guests,items in guestInfo.items():
        counter=counter+ items.get(itemName,0)        #get method searches for key, default=0       
    totalcount = str(counter)
    print('The count of  '+ itemName + ' is ' + totalcount)
    return counter

print(guestInfo)
print('Which item would you like to know the count of?')
name=input()
totalItems(guestInfo,name)
