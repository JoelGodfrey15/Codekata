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
    a=input("enter Number:")
    if a.isdigit():
        b=a[::-1]
        if a==b:
            print('Palindrome')
        else:
            print('Not Palindrome')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()
