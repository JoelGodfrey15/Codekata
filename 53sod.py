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
    a=int(input('Enter a no.:'))
    a=str(a)
    s=0
    for i in range(len(a)):
        b=int(a[i])
        s+=b
    print(s)

if __name__ == '__main__':
    main()
