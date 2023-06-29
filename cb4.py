def FindIntersection(strArr):
    intersection = []
    for i in strArr[0].split(','):
        for j in strArr[1].split(','):
            if i == j:
                intersection.append(i)
    if intersection == []:
        print(False)
    else:
        print(intersection)

#   return strArr

# keep this function call here 
# print(FindIntersection(input()))


FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])



