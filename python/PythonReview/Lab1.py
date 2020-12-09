# Lab 1 - Jared Jamieson

# Takes a list of numbers and returns the difference
def  difference(givenlist):
    # Counting variables
    maxnum = givenlist[0]
    minnum = givenlist[0]

    # Check each number in list, save if significant
    for element in givenlist:
        if element > maxnum:
            maxnum = element
        elif element < minnum:
            minnum = element

    # Difference equation
    diff = maxnum - minnum

    return diff


# Takes positive integer and returns sum of all even numbers less than given integer
def sum_even_cubes(givennum):
    # Temporary variable for function
    tempVar = 0
    counter = 2
    
    # Tree to find all even cubes less than given number
    while counter < givennum:
        tempVar += counter**3
        # Base Case
        counter += 2
        
    return tempVar


# Takes a list and returns Boolean for repetition
def has_duplicate(givenlist):
    # Temporary list for function
    tempList = []
    
    # Checks is element is already in temp list
    for element in givenlist:
        if element in tempList:
            return True
        else:
            tempList.append(element)
            
    return False


# Takes two lists and returns list of values multiplied at same index
def list_product(givenlist, givenlist2):
    # Temporary list of products
    productlist = []
    count = len(givenlist)
    # Multiplies same position of each list
    for i in range(count):
        productlist.append(givenlist[i] * givenlist2[i])

    return productlist

def main():
    #givenlist = [1,2,3]
    #givenlist2 = [4,5,6]
    #givennum = 2

    #print(difference(givenlist))
    #print(sum_even_cubes(givennum))
    #print(has_duplicate(givenlist))
    #print(list_product(givenlist, givenlist2))

main()


