#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     29-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=input('Type in something:')
    if a.isnumeric():
        print('Numeric')
    else:
        print('Not Numeric')

if __name__ == '__main__':
    main()
