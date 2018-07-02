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
    a=input('Enter no:')
    l=1
    for i in range(len(a)):
        l=l*int(a[i])
    print(l)

if __name__ == '__main__':
    main()
