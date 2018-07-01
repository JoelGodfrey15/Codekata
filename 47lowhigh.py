#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     01-07-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n=int(input('Enter no. of elements:'))
    a=[]
    high=0
    low=0
    for i in range(n):
        a.append(int(input('Enter element:')))
    for i in range(1,n):
        if a[i]<a[low]:
            low=i
        elif a[i]>a[high]:
            high=i
        else:
            pass
    print(a[low],' ',a[high])


if __name__ == '__main__':
    main()
