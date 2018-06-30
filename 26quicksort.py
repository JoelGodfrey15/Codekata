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
    n=int(input('Enter no. of elements:'))
    a=[]
    for i in range(n):
        a.append(int(input('Enter the element:')))
    a=quickSort(a,0,n-1)
    print(a)


def quickSort(arr,start,end):
    if start<end:
        mid=partition(arr,start,end)
        quickSort(arr,start,mid-1)
        quickSort(arr,mid+1,end)
    return arr

def partition(arr,start,end):
    pivot = end
    mid = start
    for i in range(start,end):
        if arr[i]<=arr[pivot]:
            arr[i],arr[mid]=arr[mid],arr[i]
            mid+=1

    arr[mid],arr[pivot]=arr[pivot],arr[mid]
    return mid


if __name__ == '__main__':
    main()
