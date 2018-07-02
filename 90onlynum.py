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
    a=input('Enter anything:')
    b=len(a)
    l=[]
    for i in range(b):
        if a[i].isnumeric():
            l.append(a[i])
    q=''.join(l)
    print(q)


if __name__ == '__main__':
    main()
