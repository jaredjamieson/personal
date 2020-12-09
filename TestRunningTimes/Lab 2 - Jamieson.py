'''
Jared Jamieson
Code for Lab 2 from textbook
lab2.py
'''

import timeit
import random

####### Code for Part II #######

def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):                  # loop from 0 to n-1
        total += S[j]
    return total

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):            # note the increment of 2
        total += S[j]
    return total

def example3(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):                  # loop from 0 to n-1
        for k in range(1+j):            # loop from 0 to j
            total += S[k]
    return total

def example4(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

def example5(A, B):                     # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    for i in range(n):                  # loop from 0 to n-1
        total = 0
        for j in range(n):              # loop from 0 to n-1
            for k in range(1+j):        # loop from 0 to j
                total += A[k]
        if B[i] == total:     ### IndexError: List index out of range ###
            count += 1
    return count

####### Code for Part III #######

def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                         # create new list of n zeroes
    for j in range(n):
        total = 0                       # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1)            # record the average
    return A

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                         # create new list of n zeroes
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)    # record the average
    return A

def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                         # create new list of n zeroes
    total = 0                           # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]                   # update prefix sum to include S[j]
        A[j] = total / (j+1)            # compute average based on current sum
    return A


def main():

    #n = 500    # Sample Sizes Part 2B
    #n = 750
    #n = 1000
    #n = 1500
    #n = 2000
    
    #n = 10000     # Sample Sizes Part 2C
    #n = 50000
    #n = 100000
    #n = 500000
    #n = 1000000
    #n = 10000000
    
    #n = 100     # Sample Size Part 3A
    #n = 1000
    #n = 10000
    #n = 100000
    
    S = []   # Create empty list to store rand ints
    
    for i in range(n):   # Run for n times
        S.append(random.randint(0, 10 * n))    # Pick and add rand int to list S
    
    # Timer begins
    start_time = timeit.default_timer()
    
    # Code
    #example1(S)
    #example2(S)
    #example3(S)
    #example4(S)
    #example5(S, S)
    
    #prefix_average1(S)
    #prefix_average2(S)
    #prefix_average3(S)
    
    
    end_time = timeit.default_timer()
    time_elapsed = end_time - start_time # Timer ends and calculates elapsed time
    
    print(time_elapsed)
    

main()