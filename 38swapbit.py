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
    a = int(input('Enter first no.'))
    b = int(input('Enter Second no.'))
    a=a^b
    b=a^b
    a=a^b
    print(a)
    print(b)

if __name__ == '__main__':
    main()
