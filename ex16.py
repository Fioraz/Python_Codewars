# Scoring Tests

# Option 1
def scoring(tests, right, omit, wrong):
    rcount = tests.count(0)
    ocount = tests.count(1)
    wcount = tests.count(2)
    return rcount * right + ocount * omit - wcount * wrong


# Option 2
def score_test(tests, right, omit, wrong):
    return tests.count(0) * right + tests.count(1) * omit - tests.count(2) * wrong 


scoring([0, 0, 0, 0, 2, 1, 0], 2, 0, 1)