# Script: bubble-sort.py
# Author: Joseph L. Crandal
# Purpose: Demonstrate bubble sort

# data will be the list to be sorted
data = [ 0, 5, 2, 3, 10, 123, -53, 23, 9, 2 ]
dataOrig = [ 0, 5, 2, 3, 10, 123, -53, 23, 9, 2 ]

# In a bubble sort you will work your way through the dataset
# and move the elements that are adjacent

def bubbleSort(arr):
    # Get the length of the array so we know how far to look
    length = len(arr)

    for i in range(length):
        # changed will let us keep track of whether anything was changed on the last pass
        changed = False
        # The range is going to be the length minus what we have already been through minus 1
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
               # Swaps the position of the two elements so the lower value is lower in the order
               arr[j], arr[j+1] = arr[j+1], arr[j]
               changed = True
        # To avoid unneeded processing we break if no changes were made, meaning it is done sorting
        if changed == False:
            break

# Execute the sort
bubbleSort(data)

# Show sorted array versus original
print("Unsorted array: ")
for i in range(len(dataOrig)):
    print(dataOrig[i])
print("Sorted array: ")
for i in range(len(data)):
    print(data[i])
