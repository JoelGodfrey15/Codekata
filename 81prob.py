#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     03-07-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    l=[]
    b=[]
    f=[]
    a=' '
    while(a!=''):
        l.append(a)
        a=input('Enter the 2 no with a blankspace inbetween:')

    for i in l[1:]:
        for j in range(len(i)):
            if i[j]==' ':
                b.append(int(i[:j]))
                b.append(int(i[j+1:]))
                break

    for i in range(0,len(b),2):
        c=abs(b[i]-b[i+1])
        f.append(c)
        i+=2

    for i in f:
        print(i)



if __name__ == '__main__':
    main()
