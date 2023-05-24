#Highest and Lowest

# Option 1
def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split(' ')]
    return f"{max(num_list)} {min(num_list)}"


# Option 2
def high_and_low(numbers):
    num_list = list(numbers.split(' '))
    int_lst = []
    for num in num_list:
        int_lst.append(int(num))
    high = max(int_lst)
    low = min(int_lst)
    return f'{high} {low}'


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

