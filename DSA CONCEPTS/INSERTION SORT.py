def insertion_sort(arr):
   n=len(arr)
   for i in range(1,n):
       key=arr[i]
       j=i-1
       while j>=0 and key<arr[j]:
           arr[j+1]=arr[j]
           j-=1
           arr[j+1]=key
my_list=[66,36,25,12,22,11,90]
print("Original list:",my_list)
insertion_sort(my_list)
print("sorted list:",my_list)
