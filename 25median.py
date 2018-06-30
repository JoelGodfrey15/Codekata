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
    n=int(input('Enter number elements'))
    l=[]
    for i in range(n):
        l.append(int(input('Enter the element')))
    a=sorted(l)
    if n%2!=0:
        x=int((n+1)/2)-1
        med=a[x]
        print(med)
    else:
        x=int(n/2)-1
        med=(a[x]+a[x+1])/2
        print(med)


if __name__ == '__main__':
    main()
