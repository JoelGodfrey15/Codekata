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
    k=int(input('Enter the no. to be checked'))
    a=[]
    s=0
    for i in range(n):
        a.append(int(input('Enter the elements')))
    for i in range(n):
        if a[i]==k:
            s=1
            print('Yes')
            break
    if s==0:
        print('No')

if __name__ == '__main__':
    main()
