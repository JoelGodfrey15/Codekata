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
    s=0
    if a==2 or a==3 or a==1 or a==0:
        print('No')
    elif a%2==0:
        print ('Yes')
    else:
        for i in range (3,a,2):
            if a%i==0:
                print('Yes')
                break
            else:
                s=1
        if s==1:
            print('No')


if __name__ == '__main__':
    main()
