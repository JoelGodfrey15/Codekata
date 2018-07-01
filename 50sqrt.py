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
    a=int(input('Enter string:'))
    b=a
    while(b>1):
        b=b/2
        if b%1==0:
            s=1
        else:
            s=0
    if s==1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
