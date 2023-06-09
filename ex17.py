# Counting Duplicates
# Option 1

def func(string):
    string = string.lower()
    duplicates = list(set([item for item in string if string.count(item) > 1]))
    return len(duplicates)


func("aA11")