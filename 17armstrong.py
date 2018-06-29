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
    a=input('Enter a number')
    s=0
    for i in range(len(a)):
        x=int(a[i])
        s=s+x**3
    if s==int(a):
        print ('Armstrong Number')
    else:
        print('Not a Amrstrong Number')

if __name__ == '__main__':
    main()
