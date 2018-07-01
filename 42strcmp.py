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
    a=input('Enter string:')
    b=input('Enter string:')
    if len(a)>len(b):
        print(a)
    elif len(a)<len(b):
        print(b)
    else:
        print(a or b)


if __name__ == '__main__':
    main()
