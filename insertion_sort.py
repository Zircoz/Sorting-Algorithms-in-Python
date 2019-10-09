# Insertion Sort Implementation

# Main function that takes 
# arr --> Array to be sorted
def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
        
        # get current element
        key = arr[i] 
  
        # Move elements that are greater than key
        # to one position ahead of their current position 
        j = i - 1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
# Test
arr = [12, 11, 13, 5, 6, 9, 8] 
print ("Original array is: {}".format(arr)) 
insertionSort(arr) 
print ("Sorted array is: {}".format(arr)) 