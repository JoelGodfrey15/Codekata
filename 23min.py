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
    a=int(input('Enter no. of elements'))
    l=[]
    for i in range(a):
        l.append(int(input('Enter the element')))
    print(min(l))


if __name__ == '__main__':
    main()
