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
    a=input('Enter number:')
    if not a.isdigit():
        print ('Invalid')
    else:
        a=int(a)
        if (a%2==0):
            print ('Even')
        elif (a%2==1):
            print ('Odd')

if __name__ == '__main__':
    main()
