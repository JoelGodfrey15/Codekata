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
    a=int(input('Enter a no.:'))
    if a%2==0:
        print(a)
    else:
        print(a-1)

if __name__ == '__main__':
    main()
