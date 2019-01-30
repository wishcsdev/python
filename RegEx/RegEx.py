#! Python3

# identifying dob using reg ex in a string

import re 
                                          # \d is integer format
format=re.compile(r'\d\d\d\d-\d\d-\d\d')  #variable that stores the regex object format

match=format.search('My dob is 1987-01-01') #search this sentence for the format variable
dob=match.group()                             #the result is grouped together

print("DOB= " +dob)

#-----------------------------------------------------------------------
format2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)| (Superman) ')    # object with 2 groups and a PIPE of 2 searches 
                                                                        # Pipe only returns one of the results
                                                                        #note the extra parentheses in first bracket d\
match2= format2.search('Superman phone number is (403) 470-9474 ')
#areaCode=match2.group(1)
#number=match2.group(2)
#entireNumber=match2.group(0)
print('My area code is '+match2.group(1)+ '\n' +'My number is ' +match2.group(2)+ '\nI am ' +match2.group())

#--------------------------------------------------------------------------

#use of built in character classes 
#finall method returns all instances of the search, not just the first. `

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

#-----------------------------------------------------------------------------

#create  my own Regex Character Class!

vowelRegex = re.compile(r'[aeiouAEIOU]')                #case sensitive
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#-------------------------------------------------------------------------------

#regex for email from clipboard
import pyperclip

clip=str(pyperclip.paste())             #clipboard copy
email=re.compile(r'''([\w\.-]+          
                    @[\w\.])''')        #regex pattern 
found=email.findall(clip)               #find anything that looks like the regex pattern

for emails in found:
    print ('/n'+ emails)
