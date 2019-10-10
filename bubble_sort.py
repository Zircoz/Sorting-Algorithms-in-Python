def bubble_sort(arr):
    #finding the length of the list which is to be sorted
    size = len(arr)

    for i in range(size):
        for j in range(0, size-i-1):

            '''swap is made false considering the list 
            to be already sorted in the first place'''
            swap = False     

            if arr[j] > arr[j+1]:                       #comparing two consecutive values 
                arr[j], arr[j+1] = arr[j+1], arr[j]     #swapping those values 
                swap = True                             #swap is made true as the consecutive values are swapped
        
        #quit the loop if no swaps took place during any iteration
        if swap == False:
            break  

    return arr

arr = [9, 5, 1, 3, 8, 6]
sorted_arr = bubble_sort(arr)
print(sorted_arr)