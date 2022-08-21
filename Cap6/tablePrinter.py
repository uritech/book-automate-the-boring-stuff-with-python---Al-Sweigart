"""Write a function named printerTable() that takes a list of lists of strings and 
displays it in a well-organized table with each column
right-justified. Assume that all the inner lists will contain the same number of strings."""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):

    #Creates a list containing the same number of 0 values as the number
    #of inner lists in tableData
    colWidths = [0] * len(table)
    for index, value in enumerate(table):
        #We use a for loop inside the max() method to find the longest string
        colWidths[index] = max(len(v) for v in value)
    
    #We use this for loop in order to print tableData[0][0], tableData[1][0], tableData[2][0] and so on.
    for y in range(len(table[0])):
        for x in range(len(table)):
            print(table[x][y].rjust(colWidths[x]), end = ' | ')
        print()

printTable(tableData)