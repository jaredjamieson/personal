# Jared Jamieson
# Lab 12 Sorting

import sorting, timeit, random

def r_int(N):
    ### Return Random List of 10*N ###
    int_list = []
    for num in range(N):
        int_list.append(random.randint(0, 10*N))
    return int_list

def s_int(N):
    ### Returns Sorted List of 10*N ###
    return list(range(N))

def b_int(N):
    ### Returns Reversed Sorted List of 10*N ###
    return list(range(N, 0, -1))

def main():
    ### Part A, B ###
    funcs = [sorting.radix_sort]
    #funcs = [sorting.selection_sort, sorting.insertion_sort, sorting.bubble_sort] #, sorting.quick_sort
    N = 100000  # List size
    print('List Size: %d' % N)
    
    for i in range(len(funcs)):  # Test each function in funcs
        start_time = timeit.default_timer()

        funcs[i](b_int(N))  # [rand, sort, backwards] test current function with list type
        
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time  # Calculate run time
        
        print('Time Elapsed: %f seconds' % time_elapsed)  # Print time and function used
        print('Function Type: %s' % str(funcs[i]))

main()