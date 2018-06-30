#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     30-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=int(input('Enter First no.'))
    b=int(input('Enter Second no.'))
    a,b=b,a
    print(a,' ',b)

if __name__ == '__main__':
    main()
