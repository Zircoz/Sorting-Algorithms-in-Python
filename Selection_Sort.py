# Selection Sort
'''
Inside the function create a loop with a loop variable i that counts from 0 to the length of the list – 1.
Create a variable smallest with initial value i.
Create an inner loop with a loop variable j that counts from i + 1 up to the length of the list – 1.
Inside the inner loop, if the elements at index j is smaller than the element at index smallest, then set smallest equal to j.
After the inner loop finishes, swap the elements at indexes i and smallest.

Author: Shriya Madan & Kaushal Agarwal
'''

#Improvement in input methods
'''
To take different type of input " list_input() " main method is called in Driver Code. 
It provides to possible option to user as either user enter the length of array or  not.
if user enter length of array then array takes input for user until length of reached in different interactive form. Some example are given below:-
example length of array  is 10 
input format 1-
2 3 2 5  5 65 7 4 10 966

input format 2-
52 363
12 3365
1252 6662 545322
12 3
56

input format 3-
23
45
12
52
32
85
10
12
32
52

if user choose option second to not specify the length of array then array store input untill 'user enter '$' or any character except integer or float'
input format 1-
2 3 2 5  5 65 7 4 10 966 $

input format 2-
52 363
12 3365
1252 6662 545322
12 3
56 $

input format 3-
23
45
12
52
32
85
10
12
32
52
$
Improved by Kaushal Agarwal
'''


def with_length():
    flag = 1
    while(flag):
        print("Length of array")
        try:
            n = int(input())
            flag=0
        except:
            flag=1

    print("It only store first ",n," elements.")
    print("\nEnter your elements.")
    arr =[]
    while len(arr)<n:
        val = list(map(float,input().split()))
        length = n - len(arr)
        if len(val)>length:
            arr = arr+val[:length]
        else:
            arr = arr+val
    return arr
def without_length():
    print("Array only takes integer or float inputs. Enter '$' to stop")
    arr = list(map(float,input().split()))
    while(1):
        val = input().split()
        for x in val:
            try:
                x = float(x)
            except:
                return arr
            arr.append(float(x))


def list_input():
    ch =""
    while ch not in ['y','n','Y','N']:
        print("Want to specify the length of arry y/n ",end=' ')
        ch = input()
    if ch=='Y' or ch=='y':
        arr = with_length()
        return arr
    else:
        arr= without_length()
        return arr


def selection_sort(alist):
    """
    Sorts a given list using a selection sort algorithm
    :param alist: a list to be sorted
    :return: None
    """

    for i in range(0, len(alist) - 1):         # loop for number of elements in alist
        smallest = i                           # smallest holds the value of i
        for j in range(i + 1, len(alist)):     
            if alist[j] < alist[smallest]:     # comparing if value at index j is smaller
                smallest = j                   # then insert value of j in smallest(so we will get smallest value in this)
        alist[i], alist[smallest] = alist[smallest], alist[i]     # swapping value of smallest and i


if __name__ == '__main__':

    arr = list_input()   # improved way of taking input us list_input()
    print ('Given array is', end='\n')
    print(*arr)

    selection_sort(arr)

    print('Sorted array is:', end='\n')
    print(*arr)
