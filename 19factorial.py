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
    s=1
    if a==0:
        print(s)
    else:
        for i in range(1,a+1):
            s=s*i
        print(s)

if __name__ == '__main__':
    main()
