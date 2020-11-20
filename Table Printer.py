'''
Automate the boring Stuff
Chapter 6 question Table Printer.

The following code can transpose a matrix or 2D list in python.

This code also spaces out the output list to be easily read.
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

#Transpose Grid
def transpose(grid):
    for m in range(len(grid[0])):       #Loop the the bottom of Column
        print()                         #Print New line
        for n in range(len(grid)):      #Loop to end of row
            print (grid[n][m],end=",")  #Print[X:Y] position of matrix add sep
            n+=1                        #Move to next column in row
    m+=1                                #Move to next row

transpose(tableData)                      #Run transponing Matrix
print()

for a, b, c in zip(tableData[0], tableData[1], tableData[2]):   #space it out
    print(a.rjust(10), b.rjust(10), c.rjust(10))                #print it out
