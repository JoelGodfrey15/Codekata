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
    a=int(input('Enter the no. for 5 multiples:'))
    for i in range(1,6):
        print (a*i, end=' ')

if __name__ == '__main__':
    main()
