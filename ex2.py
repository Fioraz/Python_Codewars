# Option 1
def printer(s):
    error_count = 0
    digits = len(s)
    for x in s:
        if x > "m":
            error_count += 1
    return f"{error_count}/{digits}"



# Option 2
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))



# Option 3
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

printer("ashfnewwea")
