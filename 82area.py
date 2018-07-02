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
    l=float(input('Enter length:'))
    b=float(input('Enter breadth:'))
    a=l*b
    a=round(a,5)
    print(a)

if __name__ == '__main__':
    main()
