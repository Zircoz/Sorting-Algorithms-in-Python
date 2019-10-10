What is Insertion Sort ?
Insertion sort is an in-place sorting algorithm that works in a similar way as we sort cards in our hand in a card game.
We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put at their right place

How it works ?
Suppose we want to sort this array in ascending order:
12, 11, 13, 5, 6

Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

For i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
Array after this step:
11, 12, 13, 5, 6

For i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
Array after this step:
11, 12, 13, 5, 6

For i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
Array after this step:
5, 11, 12, 13, 6

For i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
Array after this step:
5, 6, 11, 12, 13

Thus our array gets sorted in ascending order!!


Complexity:

Worst case Complexity: O(n^2)
Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worse case complexity occers.

Best case Complexity: O(n)
When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there is only n number of comparison. Thus, complexity is linear.

Average case Complexity: O(n^2)
It occurs when the array is neither in ascending order or descending order.

Space Complexity: O(1)


Notes:
1) In windows system, execute the script by command "python insertion.py" and in a linux system use command "./insertion.py". 
2) Enter the array as space separated integers. For example:- 1 2 3 4 { Array is [1,2,3,4] }
3) The array is sorted in ascending order. 
