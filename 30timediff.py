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
    m1=int(input('Enter time in 1st mins:'))
    m2=int(input('Enter time in 2nd mins:'))
    h=[]
    h1=list(divmod(m1,60))
    h2=list(divmod(m2,60))
    for i in range(2):
        h.append(h1[i]-h2[i])
    if h[1]<0:
        h[0]=h[0]-1
        h[1]=h[1]+60
    else:
        pass
    print(h[0],' ',h[1])


if __name__ == '__main__':
    main()
