# Merge Sort
# Selection sort
# Heap sort

    
def bubble_sort(nums):
    size = len(nums)
    for _ in range(size-1):
        for i in range(1, size):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
    return nums


def insertion_sort(nums):
    pass
    return nums


def quick_sort(data, left, right): 
    if left >= right :     
        return
    i = left                     
    j = right                   
    key = data[left]              
    while i != j: 
        while data[j] > key and i < j:   
            j -= 1 
        while data[i] <= key and i < j:  
            i += 1 
        if i < j:                        
            data[i], data[j] = data[j], data[i] 
    data[left] = data[i] 
    data[i] = key 
    quick_sort(data, left, i-1)
    quick_sort(data, i+1, right) 

    
if __name__ == "__main__":
    data1 = [5, 3, 7, 1, -5, 10, 2, 13, 0]
    sort_data1 = bubble_sort(data1)
    print(sort_data1)