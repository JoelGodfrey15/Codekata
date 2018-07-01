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
    a=int(input('Enter first no.:'))
    b=int(input('Enter second no.:'))
    c=a*b
    d=c**(1/2)
    if d%1==0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
