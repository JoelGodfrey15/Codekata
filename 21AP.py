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
    n=int(input('Enter number of terms:'))
    a=int(input('Enter first term:'))
    d=int(input('Enter common diff:'))
    q=0
    i=0
    while(i<n):
        q=q+a
        a=a+d
        i=i+1
    print(q)

if __name__ == '__main__':
    main()
