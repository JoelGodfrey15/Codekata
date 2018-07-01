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
    n=int(input('Enter no. of elements:'))
    a=[]
    sum=0
    for i in range(n):
        a.append(int(input('Enter element:')))
    for i in range(n):
        sum+=a[i]
    avg=sum/n
    print(avg)

if __name__ == '__main__':
    main()
