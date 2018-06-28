#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     28-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=int(input('Enter First Number:'))
    b=int(input('Enter Second Number:'))
    c=int(input('Enter Third Number:'))
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

if __name__ == '__main__':
    main()
