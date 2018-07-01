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
    a=int(input('Enter a Number:'))
    a=str(a)
    for i in range(len(a)):
        print(a[i], end=' ')

if __name__ == '__main__':
    main()
