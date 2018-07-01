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
    a=input('Enter no.:')
    s=0
    for i in range(len(a)):
        if a[i]=='0' or a[i]=='1':
            pass
        else:
            s=1
    if s==1:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
