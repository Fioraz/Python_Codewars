# Name Shuffler
# Option 1
def name_shuffler(string):
    newlist = string.split(' ')[::-1]
    print(" ".join(newlist))


# Option 2
def name_shuffler(string):
    print(" ".join(string.split(' ')[::-1]))

name_shuffler('john McClane')