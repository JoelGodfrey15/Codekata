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
    l=input('Enter Something:')
    a=0
    n=0
    for i in range(len(l)):
        b=l[i]
        if b.isnumeric():
            n=1
        elif b.isalpha():
            a=1
    if a==1 and n==1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
