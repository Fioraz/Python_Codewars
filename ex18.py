# Simple Pig Latin
# Option 1
def pig_it(string):
    newarray = string.split(" ")
    newstring = []
    for i in range(0, len(newarray)):
        if newarray[i] != "?" and newarray[i] != "!":
            newstring.append(f"{newarray[i][1:]}{newarray[i][0]}ay")
        elif newarray[i] == "!":
            newstring.append("!")
        else:
            newstring.append("?")
    print(" ".join(newstring))



# Option 2
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])



# Option 2
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])



# Option 3
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())




pig_it('Pig latin is cool !')

