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
    if len(a)>1 or not a.isalpha() :
        print('Invalid')
    else:
        if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
            print('Vowel')
        else:
            print('Consonant')

if __name__ == '__main__':
    main()
