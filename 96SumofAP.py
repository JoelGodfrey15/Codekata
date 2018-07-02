#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     02-07-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    A=int(input('Enter first element:'))
    B=int(input('Enter common diff:'))
    C=int(input('Enter no of elements:'))
    s=C*((2*A)+((C-1)*B))/2
    print(s)

if __name__ == '__main__':
    main()
