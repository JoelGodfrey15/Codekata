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
    a=input('Enter a string')
    e=[]
    o=[]
    for i in range(len(a)-1):
        if i%2==0:
            e.append(a[i])
        else:
            o.append(a[i])
    e=''.join(e)
    o=''.join(o)
    print(e,' ',o)

if __name__ == '__main__':
    main()
