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
    a=input('Enter the no.')
    for i in range(len(a)):
        b=int(a[i])
        if b%2!=0:
            print(b, end=' ')

if __name__ == '__main__':
    main()
