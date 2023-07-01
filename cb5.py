def QuestionsMarks(strParam):
    l_number = None
    q_count = 0
    for x in str:
        if x.isnumeric():
            number = int(x)
            if l_number is not None and l_number + number == 10:
                if q_count == 3:
                    return True
            l_number = number
            q_count = 0

        elif x == "?":
            q_count += 1
    return False


            

            

# keep this function call here 
# print(QuestionsMarks(input()))
