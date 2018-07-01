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
    a=input("enter String:")
    b=a[::-1]
    if a==b:
        print('Palindrome')
    else:
        print('Not Palindrome')

if __name__ == '__main__':
    main()
