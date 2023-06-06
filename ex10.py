# Jaden Casing Strings
# Option 1
def fun(string):
    strlist = string.split(' ')
    newlist = [word.capitalize() for word in strlist]
    return " ".join(newlist)


def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

fun("sta yth gh's nt")