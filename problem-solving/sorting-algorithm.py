# my poor sorting algorithm
"""time complexity is o(n^2) which is too bad especially for larger numbers eg 1000's and above of items"""
def my_sorting(arr):
    min_val = min(arr)
    max_val = max(arr)
    sorted_arr = []
    # Building the sorted_arr
    for num in range(min_val, (max_val + 1)):
        while (num in arr):
            sorted_arr.append(num)
            arr.remove(num)

    return sorted_arr 


# bubble-sort
"""bubble sort is the most naive conventional sort algorithm that you can even teach to a chimpanzee
bubble sort is inplace implying it has space_complexity (more correctly auxiliary space complexity) 
of O(1) ie constant but the time complexity is O(n^2) implying in overall it beats my poor sorting
algorithm since my_poor sort takes an auxiliary space of O(n)"""
def my_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# quick-sort
"""
The last step in count sort the most important operation which gave me headache was 
    'sorted_arr[count[num] -1 ] = num'
    'count[num] -1 '  implies getting the index of num in sorted_array

"""
def counting_sort(arr): 
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)
    
    for num in arr:
        count[num] += 1
    # print(count)
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # print(count) # cumulative count array
    
    for num in arr[::-1]:
        sorted_arr[count[num] - 1] = num  # this is the operation
        count[num] -= 1
    
    return sorted_arr



















if __name__ == "__main__":
    print("Hello world")


