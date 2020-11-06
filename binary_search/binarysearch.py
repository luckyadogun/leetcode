def binary_search(array, target):
     array = sorted(array) #sort the array
     start = 0
     end = len(array) - 1
     while start <= end:
        middle = start + (end - start) // 2 #find the middle
        item = array[middle]
        if target == item:
            return middle
        if target < item:
            end = middle - 1
        else:
            start = middle + 1
     return None