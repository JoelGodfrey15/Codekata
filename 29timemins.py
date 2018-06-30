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
    m=int(input('Enter time in mins:'))
    h=list(divmod(m,60))
    print(h[0],' ',h[1])

if __name__ == '__main__':
    main()
