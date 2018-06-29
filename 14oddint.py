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
    n=int(input('Enter Begining no.:'))+1
    q=int(input('Enter Ending no.:'))
    a=[]
    for i in range(n,q):
        if i%2!=0:
            a.append(i)
    for i in a:
        print(i,end=' ')

if __name__ == '__main__':
    main()
