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
    a=input('Enter year:')
    if a.isdigit():
        a=int(a)
        if a%4==0:
            print('Yes')
        else:
            print('No')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()
