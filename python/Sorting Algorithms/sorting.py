# Sorting module for CS/IT 200.
# Author: Brian O'Neill
#
# Code for Selection Sort, Insertion Sort, and Bubble Sort based on Wikipedia algorithms.
# Code for Merge Sort and in-place Quick Sort modified slightly from Goodrich et. al, Chapter 12


# ------------------------ Public methods ------------------------
def selection_sort(mylist):
    """Sort the list using the selection sort algorithm"""
    for j in range(len(mylist)):
        current_min = j
        for i in range(j+1, len(mylist)):
            if mylist[i] < mylist[current_min]:
                current_min = i

        if current_min != j:
            _swap(mylist, current_min, j)


def insertion_sort(mylist):
    """Sort the list using the insertion sort algorithm"""
    for i in range(1, len(mylist)):
        x = mylist[i]
        j = i-1
        while j >= 0 and mylist[j] > x:
            mylist[j+1] = mylist[j]
            j -= 1
        mylist[j+1] = x


def bubble_sort(mylist):
    """Sort the list using the bubble sort algorithm"""
    n = len(mylist)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if mylist[i-1] > mylist[i]:
                _swap(mylist, i-1, i)
                swapped = True
        n -= 1


def merge_sort(mylist):
    """Sort the elements of mylist using the merge-sort algorithm"""
    n = len(mylist)
    if n < 2:
        return          # list is already sorted
    # divide
    mid = n // 2
    S1 = mylist[0:mid]  # copy of first half
    S2 = mylist[mid:n]  # copy of second half
    # conquer (with recursion)
    merge_sort(S1)      # sort the copy of the first half
    merge_sort(S2)      # sort the copy of the second half
    # merge results
    _merge(S1, S2, mylist)


def quick_sort(mylist):
    """Sort the elements of mylist using the quick-sort algorithm"""
    _inplace_quick_sort(mylist, 0, len(mylist)-1)


def radix_sort(mylist):
    """ Sort the elements of mylist using the radix-sort algorithm """
    max_num = max(mylist)
    position = 1    # Find decimal position
    while len(str(max_num)) <= len(str(position)):  # Go for as many decimal places in largest num
        int(position)
        counting_sort(mylist, position)  # Sort by decimal place
        position *= 10  # Increase to next left decimal place
    
    
def counting_sort(mylist, position):
    """ Sorts the elements of mylist by position """
    length = len(mylist)
    final = [0] * length    # Final sorted list
    temp = [0] * 10        # Current sorted list

    for i in range(length):  # Add last digit of element to temp
        index = mylist[i]
        temp[index % 10] += 1

    for i in range(1, 10):   # Shift over elements
        temp[i] += temp[i - 1]

    i = length - 1        # Index to last element of list
    
    while i >= 0:         # Traverse from right to left
        index = mylist[i]
        final[temp[index % 10] - 1] = mylist[i] # Add elements to final list by sorted position order
        temp[index % 10] -= 1
        i -= 1

    for i in range(length):  # Save final list back to mylist
        mylist[i] = final[i]


# ------------------------ Protected methods ------------------------

def _merge(S1, S2, mylist):
    """Merge two sorted lists S1 and S2 into properly sized mylist"""
    i = 0
    j = 0
    while i + j < len(mylist):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            mylist[i+j] = S1[i]     # Copy ith element of S1 as next item of mylist
            i += 1
        else:
            mylist[i+j] = S2[j]     # Copy jth element of S2 as next item of mylist
            j += 1


def _inplace_quick_sort(mylist, a, b):
    """Sort the list from mylist[a] to mylist[b] inclusive using quick-sort"""
    if a >= b:
        return                                  # range is trivially sorted
    pivot_index = _choose_pivot(mylist, a, b)   # select pivot index
    pivot = mylist[pivot_index]                 # get pivot value
    _swap(mylist, pivot_index, b)               # move pivot to edge
    left = a                                    # scans rightward
    right = b-1                                 # scans leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and mylist[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < mylist[right]:
            right -= 1
        if left <= right:   # scans did not cross
            _swap(mylist, left, right)  # swap
            left += 1
            right -= 1                  # shrink the range we're looking at

    # put pivot into its final place (currently marked by left index)
    _swap(mylist, left, b)
    # recurse
    _inplace_quick_sort(mylist, a, left-1)
    _inplace_quick_sort(mylist, left+1, b)


def _swap(mylist, a, b):
    """Swap elements at a and b in mylist"""
    temp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = temp


def _choose_pivot(mylist, a, b):
    """Select the pivot index for quick sort. Value must be selected from within indices a and b (inclusive)"""
    return b
    '''
    mid = (a + b) // 2                       # Find middle position
    templist = [a, mid, b]
    templist.sort()                          # Sort values
    
    if templist[1] == a:                     # Return median value
        return a
    elif templist[1] == b:
        return b
    else:
        return b - a
    '''