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
    a=int(a)
    if (a>0):
        print ('Positive')
    elif (a<0):
        print ('Negative')
    else:
        print ('Zero')

if __name__ == '__main__':
    main()
