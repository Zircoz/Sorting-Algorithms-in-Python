#ins method takes an array a and sorts in ascending.
def ins(a):
    for i in range(1,len(a)):
        tmp = a[i]
        k = i-1
        while( a[k]>tmp and k>=0):
            a[k+1] = a[k]
            k-=1
        a[k+1] = tmp


# Entering the array as space separated integers.
print("Please Enter your array as space separated integers!!")
arr = list(map(int,input().split(" ")))
ins(arr)
print("The sorted array is:")
# printing the sorted array.
for x in range(len(arr)):
    print(arr[x],end=" ")




