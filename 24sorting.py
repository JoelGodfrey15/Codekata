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
    n=int(input('Enter no. of elements:'))
    l=[]
    for i in range(n):
        l.append(int(input('Enter the element:')))
    l=sortThis(l,0,n)
    print(l)


def sortThis(a,start,end):
    for j in range(0,end):
        low=j
        for i in range(j,end):
            if a[i]<a[low]:
                low=i
        a[low],a[j]=a[j],a[low]

    return a


if __name__ == '__main__':
    main()
