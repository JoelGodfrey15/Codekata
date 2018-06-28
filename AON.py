#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joel Godfrey
#
# Created:     28-06-2018
# Copyright:   (c) Joel Godfrey 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=input('Enter a alphabet:')
    if len(a)>1 or a.isdigit() :
        print('No')
    else:
        print('Alphabet')

if __name__ == '__main__':
    main()
