#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     02-07-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n=int(input('Enter number of numbers:'))
    s=0
    for i in range(n):
        b=int(input('Enter %d no:' %(i+1)))
        s+=b
    print(s)

if __name__ == '__main__':
    main()
