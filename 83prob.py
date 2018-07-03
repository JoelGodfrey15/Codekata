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
    a=' '
    while(a!=''):
        l.append(a)
        a=input('Enter:')
    for i in l[1:]:
        print(eval(i))

if __name__ == '__main__':
    main()
