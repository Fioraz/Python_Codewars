def LongestWord(sen):

    new_list = [i for i in sen.split(' ')]
    isnum_list = []
    longest_word = ''

    for x in new_list:
        new_word = ""
        for y in range(0, len(x)):
            if x[y].isalnum():
                new_word += x[y]
        isnum_list.append(new_word)
    
    for word in isnum_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
    

# keep this function call here 
print(LongestWord("i?///// love!@ you2#%^% 779"))