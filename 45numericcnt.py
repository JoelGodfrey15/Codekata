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
    a=input('Enter number:')
    s=0
    for i in range(len(a)):
        b=a[i]
        if b.isnumeric():
            s+=1
    print(s)


if __name__ == '__main__':
    main()
