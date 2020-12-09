import vector

def main():
    # Create two Vectors of length 3
    v1 = vector.Vector(3)
    v2 = vector.Vector(3)
    
    # Assign values to v1
    v1[0] = 1
    v1[1] = 2
    v1[2] = 3
    
    # Assign values to v2
    v2[0] = 5
    v2[1] = 6
    v2[2] = 7
    
    print(v1) # Should print '<1, 2, 3>'
    print(v2) # Should print '<5, 6, 7>'
    
    # Since v1 and v2 are Vectors, Python looks for the __add__ method in the Vector class to
    # know how to add two Vector objects.
    # v1 becomes the 'self' parameter in that method, while v2 becomes the 'other' parameter.
    # The function returns a third Vector object, which we assign to v3.
    v3 = v1 + v2
    
    print(v3) # Should print '<6, 8, 10>'
    
    # Create a vector of length 1
    short_vector = vector.Vector(1)
    short_vector[0] = 99
    
    # We try to add short_vector to v1, but we can't, because Vector's __add__ method requires
    # that both Vectors have the same length. So the function *raises* a ValueError, which we
    # catch in the except block.
    try:
        bad_vector = v1 + short_vector # This will fail
        print('Successfully added v1 and short_vector') # Should not print
    except ValueError:
        print('Passed test: Cannot add vectors of different lengths') # What we expect

    print()
    test_mul_method(v1, v2) # Tests the __mul__ method that you write in Lab 1

def test_mul_method(v1, v2):
    """A series of tests for the __mul__ method in Lab 1"""
    
    print('***** STARTING TESTS OF __mul__ METHOD *****\n')
    attempt_test4 = False

    try:
        print('Starting test #1: v4 = v1 * 3')
        v4 = v1 * 3
        if type(v4) != vector.Vector:
            print('Failed test: v4 should be a Vector, not a',type(v4))
        elif str(v4) != '<3, 6, 9>':
            print('Failed test: New vector should be <3, 6, 9>, not', v4)
        elif type(v1) != vector.Vector:
            print('Failed test: v1 should still be a Vector, not a',type(v1))
        elif str(v1) != '<1, 2, 3>':
            print('Failed test: v1 should still be <1, 2, 3>, not',v1)
        else:
            print('Passed tests for v4 = v1 * 3')
            attempt_test4 = True
    except Exception as e:
        print('Failed test due to exception')
        print(e)
    print()

    try:
        print('Starting test #2: v5 = v1 * 5')
        v5 = v1 * 5
        if type(v5) != vector.Vector:
            print('Failed test: v5 should be a Vector, not a',type(v5))
        elif str(v5) != '<5, 10, 15>':
            print('Failed test: New vector should be <5, 10, 15>, not', v5)
        elif type(v1) != vector.Vector:
            print('Failed test: v1 should still be a Vector, not a',type(v1))
        elif str(v1) != '<1, 2, 3>':
            print('Failed test: v1 should still be <1, 2, 3>, not',v1)
        else:
            print('Passed tests for v5 = v1 * 5')
    except Exception as e:
        print('Failed test due to exception')
        print(e)
    print()

    try:
        print('Starting test #3: v6 = v2 * 10')
        v6 = v2 * 10
        if type(v6) != vector.Vector:
            print('Failed test: v6 should be a Vector, not a',type(v6))
        elif str(v6) != '<50, 60, 70>':
            print('Failed test: New vector should be <50, 60, 70>, not', v6)
        elif type(v2) != vector.Vector:
            print('Failed test: v2 should still be a Vector, not a',type(v1))
        elif str(v2) != '<5, 6, 7>':
            print('Failed test: v2 should still be <5, 6, 7>, not',v2)
        else:
            print('Passed tests for v6 = v2 * 10')
    except Exception as e:
        print('Failed test due to exception')
        print(e)
    print()

    try:
        print('Starting test #4: v7 = v4 * 8')
        if not attempt_test4:
            print('Failed test due to failure of first test')
            
        v7 = v4 * 8
        if attempt_test4 and type(v7) != vector.Vector:
            print('Failed test: v7 should be a Vector, not a',type(v7))
        elif attempt_test4 and str(v7) != '<24, 48, 72>':
            print('Failed test: New vector should be <24, 48, 72>, not', v7)
        elif attempt_test4 and type(v4) != vector.Vector:
            print('Failed test: v4 should still be a Vector, not a',type(v4))
        elif attempt_test4 and str(v4) != '<3, 6, 9>':
            print('Failed test: v4 should still be <3, 6, 9>, not',v4)
        elif attempt_test4:
            print('Passed tests for v7 = v4 * 8')
    except Exception as e:
        print('Failed test due to exception')
        print(e)
    
main()
    
