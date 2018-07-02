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
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    q=[]
    w=[]
    c=0
    for i in range(1,a+1):
        if a%i==0:
            q.append(i)
    for i in range(1,b+1):
        if b%i==0:
            w.append(i)
    for i in q:
        for j in w:
            if i==j:
                c=i
    print(c)





if __name__ == '__main__':
    main()
