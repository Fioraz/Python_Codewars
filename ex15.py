# Testing 1-2-3
# Option 1 
def func(arr):
    arr_length = len(arr)
    new_arr = []
    for i in range(1, arr_length + 1):
        new_arr.append(f"{i}: {arr[i-1]}")
    print(new_arr)



# Option 2
def func(arr):
    arr_length = len(arr)
    new_arr = [f"{i}: {arr[i-1]}" for i in range(1, arr_length + 1)]
    print(new_arr)




func(["a", "b", "c"])