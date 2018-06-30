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
    n=int(input('Enter no. of elements'))
    a=1
    b=0
    for i in range(n):
        c=a+b
        print(c, end=' ')
        a=b
        b=c


if __name__ == '__main__':
    main()
