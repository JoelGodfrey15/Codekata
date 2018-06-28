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
    a=input('Enter number')
    if a.isdigit():
        print(len(a))
    else:
        print('Invalid')

if __name__ == '__main__':
    main()
