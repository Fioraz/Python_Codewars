# Sum - Square Even, Root Odd

# Option 1
def sum_square_even_root_odd(nums):
    new_list = []
    for n in nums:
        if n % 2 == 0:
            new_list.append(n ** 2)
        else:
            new_list.append(n ** 0.5)
    print(round(sum(new_list), 2))


# Option 2
def sum_square_even_root_odd(nums):
    return round(sum(n ** 2 if n % 2 == 0 else n ** 0.5 for n in nums), 2)


sum_square_even_root_odd([4, 5, 7, 8, 1, 2, 3, 0])