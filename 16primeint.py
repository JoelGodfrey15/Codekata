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
    n=int(input('Enter Begining no.:'))
    q=int(input('Enter Ending no.:'))
    a=[]
    s=0
    for i in range(n,q):

        if i==2 or i==3:
            a.append(i)
        elif i==1 or i%2==0:
            pass
        else:
            for j in range (3,i,2):
                if i%j==0:
                    break
                else:
                    s=1
            if s==1:
                a.append(i)
                s=0

    for i in a:
        print(i,end=' ')


if __name__ == '__main__':
    main()
