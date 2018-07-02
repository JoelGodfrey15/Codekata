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
    p=float(input('Enter Principal:'))
    n=float(input('Enter no of years:'))
    r=float(input('Enter the rate in %:'))
    si=(p*n*r)/100
    print(si)


if __name__ == '__main__':
    main()
