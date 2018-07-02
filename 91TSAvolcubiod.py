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
    l=float(input('Enter Length:'))
    b=float(input('Enter breadth:'))
    h=float(input('Enter height:'))
    tsa=2*((l*b)+(b*h)+(h*l))
    vol=l*b*h
    print(tsa,' ',vol)



if __name__ == '__main__':
    main()
