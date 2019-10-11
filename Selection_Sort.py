#Selection Sort
'''
Inside the function create a loop with a loop variable i that counts from 0 to the length of the list – 1.
Create a variable smallest with initial value i.
Create an inner loop with a loop variable j that counts from i + 1 up to the length of the list – 1.
Inside the inner loop, if the elements at index j is smaller than the element at index smallest, then set smallest equal to j.
After the inner loop finishes, swap the elements at indexes i and smallest.

Author: Shriya Madan
'''



def selection_sort(alist):                     #selection sort function 
    for i in range(0, len(alist) - 1):         #loop for number of elements in alist
        smallest = i                           #smallest holds the value of i
        for j in range(i + 1, len(alist)):     
            if alist[j] < alist[smallest]:     #comparing if value at index j is smaller 
                smallest = j                   #then insert value of j in smallest(so we will get smallest value in this)
        alist[i], alist[smallest] = alist[smallest], alist[i]     #swapping value of smallest and i
 
alist = input('Enter the list of numbers: ').split()     #taking user inputs
alist = [int(x) for x in alist]                          
selection_sort(alist)                                    #elements passed to the function for sorting
print('Sorted list: ', end='')    
print(alist)                                             #sorted array is printed
