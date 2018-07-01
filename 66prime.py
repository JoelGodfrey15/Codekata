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
    a=int(input('Enter any number:'))
    s=0
    if a==2 or a==3:
        print('Prime Number')
    elif a%2==0 or a==1:
        print ('Not a Prime Number')
    else:
        for i in range (3,a,2):
            if a%i==0:
                print('Not a Prime Number')
                break
            else:
                s=1
        if s==1:
            print('Prime Number')


if __name__ == '__main__':
    main()
