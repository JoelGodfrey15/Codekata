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
    if c%2==0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    main()
