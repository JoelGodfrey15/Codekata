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
    a=input('Enter Isogram:')
    s=0
    for i in range(len(a)-1):
        b=a[i]
        for j in range(0,len(a)):
            if a[j]==b and i!=j:
                print('No')
                s=1
                return
    if s==0:
        print('Yes')


if __name__ == '__main__':
    main()
