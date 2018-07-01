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
    a=input('Enter string:')
    b=len(a)
    l=[]
    for i in range(b):
        l.append(a[i])
    if b%2==0:
        c=int(b/2)
        l[c]=l[c-1]='*'
    else:
        c=int(b/2)
        l[c]='*'
    q=''.join(l)
    print(q)


if __name__ == '__main__':
    main()
