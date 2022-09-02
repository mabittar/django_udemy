
def prob_1(list_to_check):
    """
    Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
    """
    for i in range(len(list_to_check) - 2):
        if list_to_check[i] == 1 and list_to_check[i + 1] == 2 and list_to_check[i + 2] == 3:
            return True
    return False

def prob_2(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end
    of the other string, ignoring upper/lower case differences (in other words, the
    computation should not be "case sensitive").
    """
    a.lower()
    b.lower()
    
    return a.endswith(b) or b.endswith(a)
    

if __name__ == '__main__':
    result_1 = prob_1([1, 1, 2, 3, 1])
    assert result_1
    
    result_2 = prob_2('Hiabc', 'abc')
    assert result_2