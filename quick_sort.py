def quick_sort(arr):
    if (len(arr) < 2):
        return arr
    else:
        pivot = arr[0]  # pivot is considered to be the first element

        # now starting from element 1 (i.e., from the second element) to the end
        rest = arr[1 : ]

        # elements smaller than the pivot
        low = [each for each in rest if each < pivot]

        #elements greater than the pivot
        high = [each for each in rest if each >= pivot]

        '''now merge them calling the quicksort method recursively
        on each of the two lists (i.e., low and high)'''
        return quick_sort(low) + [pivot] + quick_sort(high)


arr = [9, 5, 1, 3, 8, 6]
sorted_arr = quick_sort(arr)
print(sorted_arr)