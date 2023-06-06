# Product of Largest Pair
# Option 1
def max_product(a):
    a.sort(reverse = True)
    return a[0] * a[1]


#Option 2


max_product([39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411])