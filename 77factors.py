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
    a=int(input('Enter a number:'))
    for i in range(1,a+1):
        if a%i==0:
            print(i, end=' ')



if __name__ == '__main__':
    main()
