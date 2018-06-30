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
    n=int(input('Enter no. of elements:'))
    a=[]
    for i in range(n):
        a.append(input('Enter the element:'))
    for i in range(n):
        print(a[i],' ',i)

if __name__ == '__main__':
    main()
