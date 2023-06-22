def FirstFactorial(num):
    factorial = 1
    while num >= 1:
        factorial *= num
        num -= 1
    print(factorial)

FirstFactorial(8)