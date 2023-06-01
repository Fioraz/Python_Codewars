# Option 1 =>> Basic Method
def xo(s):
    s = s.lower()
    x_count = 0
    o_count = 0
    for i in s:
        if i == "x":
            x_count += 1
        if i == "o":
            o_count += 1
    x_count == o_count

# Option 2 =>> Clever Method
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


xo("xoXox")