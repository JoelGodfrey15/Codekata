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
    a=input('Enter a number:')
    l=[]
    for i in range(len(a)):
        l.append(a[i])
    l.reverse()
    b=''.join(l)
    print(b)


if __name__ == '__main__':
    main()
