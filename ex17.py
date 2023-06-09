# Counting Duplicates
# Option 1

def func(string):
    string = string.lower()
    duplicates = list(set([item for item in string if string.count(item) > 1]))
    return len(duplicates)

# Option 2
def func(string):
    return len([item for item in set(string.lower()) if string.lower().count(item) > 1])


func("aA11")