# Option 1
def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    arr_sum = sum(arr) - max(arr) - min(arr)
    return arr_sum
    

# Option 2
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])


sum_array([-3, -5])