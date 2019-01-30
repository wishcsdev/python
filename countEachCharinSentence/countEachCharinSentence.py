#dictionary use
import pprint


message= "There was once a dog who loved every human. But he loved his owner more than anything else in the world"
tally={}    #dictionary

for i in message:
    tally.setdefault(i, 0)      #if i doesnot exist, assign 0
    tally[i]=tally[i]+1         #for the character, 

#print(count)
pprint.pprint(tally)        #vertical formatting
