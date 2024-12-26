
def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            # Assume current index as minimum index
            min_index = i
            for j in range(i+1,n) :
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i] , arr[min_index] = arr[min_index] ,arr[i]
        return arr
arr = [5,7,9,4,3,2,6,0,2,3,1]
print(selection_sort(arr))
