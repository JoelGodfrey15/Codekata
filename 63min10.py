#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     30-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=[]
    for i in range(9):
        a.append(int(input('Enter 10 nos.:')))
    low=0
    for i in range(1,9):
        if a[low]>a[i]:
            low=i
    print(a[low])

if __name__ == '__main__':
    main()
