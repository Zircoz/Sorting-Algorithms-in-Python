"""
    COUNTING SORT ALGORITHM

        Assumption :
        1. Element of array should be integer
        2. Each integer should be in the range of [0, 10000000]

        Time Complexity : O(max_value)
        Space Complexity : O(max_value)
"""

def countingSort(unsorted_arr):
    """ Sort natural number by counting sort algorithm """
    max_value = max(unsorted_arr)
    # Create a count array kind of like the hash map of size max_value
    count = [0 for _ in range(max_value + 1)]
    for x in unsorted_arr:
        # Get the count of each element of the unsorted array
        count[x] += 1

    # Store element in non-decreasing order
    sorted_arr = []
    for x in range(max_value+1):
        # Since we are iterating in ascending order, hence it is known for sure that 
        # anay element which is going to append to the "sorted_arr" will be in sorted array
        for y in range(count[x]):
            sorted_arr.append(x)

    return sorted_arr

# Get a list of integer from the user
unsorted_arr = list(map(int, input().strip().split()))
# Print sorted list of integer
print(*countingSort(unsorted_arr))