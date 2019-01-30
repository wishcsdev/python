#! python3

#right aligned list of lists containing strings

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs','ajkadfhkljahd', 'cats', 'moose']]

def printTable(list):
    longestString=[0]*len(list)        #new list that is [0,0,0,....] columnwidth
                                            # 0 is the initial value of the longest word.

    for l in range(len(list)):              #1st list
        for m in range(len(list[l])):       #2nd list in l
            if len(tableData[l][m]) > (longestString[l]):
                longestString[l] = len(tableData[l][m])         #update the list value if true
            else: continue
        print('Longest word is '+str(longestString[l]))

# assuming each inner list is the same length as the first, iterate over the input list
# printing the x value from each inner list, right justifed to its corresponding value
# in colWidths

    for i in range(len(list[0])):           #since the length of first row is the same as next, 
                                            #  we take length of the first row as constant
        for m in range (len(list)):         #iterate through the entire list
            print (tableData[m][i].rjust(longestString[m]),end=' ')
        print('')
printTable(tableData)


