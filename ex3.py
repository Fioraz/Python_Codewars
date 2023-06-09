# Who likes it?

# Option 1
def fun(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} likethis"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


fun(["Alex", "Jacob", "Mark", "Max"])