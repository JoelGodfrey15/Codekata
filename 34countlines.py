#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     30-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=input('Enter something:')
    n=len(a)
    c=0
    for i in range(n):
        if a[i]=='.' and a[i+1]!='.':
            c+=1
    print(c)

if __name__ == '__main__':
    main()
