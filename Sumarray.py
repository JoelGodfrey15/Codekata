#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     29-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n=int(input('Enter number of elements:'))
    k=int(input('Number of elements to be added:'))
    a=[]
    s=0
    for i in range (n):
        x=int(input('Enter the element'))
        a.append(x)

    for i in range (k):
        s=s+a[i]
    print (s)

if __name__ == '__main__':
    main()
