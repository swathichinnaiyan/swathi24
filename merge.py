def merge_sort(list1, start, end):
    
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(list1, start, mid)
        merge_sort(list1, mid, end)
        merge_list(list1, start, mid, end)
 
def merge_list(list1, start, mid, end):
    left = list1[start:mid]
    right = list1[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            list1[k] = left[i]
            i = i + 1
        else:
            list1[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            list1[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            list1[k] = right[j]
            j = j + 1
            k = k + 1
 
 
list1 = input().split()
list1 = [int(x) for x in list1]
merge_sort(list1, 0, len(list1))
print('Sorted list: ', end='')
print(list1)
