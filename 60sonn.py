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
    n=int(input('Sum of how many natural numbers:'))
    s=0
    for i in range(1,n+1):
        s+=i
    print(s)

if __name__ == '__main__':
    main()
