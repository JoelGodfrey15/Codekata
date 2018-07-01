#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     01-07-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n=int(input('Enter no.:'))
    l=int(input('Enter left end:'))
    r=int(input('Enter right end:'))
    if n>l and n<r:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
