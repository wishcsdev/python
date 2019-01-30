# Read csv file and create list of lists to be printed 
import csv
import codecs

with open('AppleStore.csv','r', encoding = 'cp1252') as file:
    readMe=csv.reader(file)
    csvList= list(readMe)
    #print (file)
print (csvList)

