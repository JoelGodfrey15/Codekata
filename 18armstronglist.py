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
    a=input('Enter the begining no.:')
    a1=int(a)
    b=input('Enter the ending no.:')
    b1=int(b)
    l=[]
    for i1 in range(a1,b1):
        i=str(i1)
        s=0
        for j in range(len(i)):
            x=int(i[j])
            s=s+x**3
        if s==int(i):
            l.append(i)
        else:
            pass
    print('Armstrong numbers are')
    for i in range(len(l)):
        print(l[i],end=' ')

if __name__ == '__main__':
    main()
