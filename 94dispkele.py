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
    n=int(input('Enter no of numbers:'))
    k=int(input('Should display which element'))
    a=[]
    for i in range(n):
        a.append(int(input('Enter no %i' %(i+1))))
    print(a[k-1])


if __name__ == '__main__':
    main()
