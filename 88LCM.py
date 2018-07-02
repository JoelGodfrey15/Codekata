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
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    if a==b:
        print(a)
    else:
        s='loop'
        if a>b:
            a,b=b,a
        c=b
        while(s=='loop'):
            if c%b==0 and c%a==0:
                print(c)
                s='no loop'
            else:
                c+=1

if __name__ == '__main__':
    main()
