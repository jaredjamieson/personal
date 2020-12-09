# Jared Jamieson
# CS/IT 201

# Imports
import binary_search_tree, timeit


class Term():
    """ A class that represents an autocomplete term """
    
    def __init__(self, query, weight):
        """ Constructor """
        if query == None:
            raise TypeError('Query cannot be None')
        if weight < 0:
            raise ValueError ('Weight cannot be negetive')
        # Self Variables
        self._query = query
        self._weight = weight
        
        
    def get_weight(self):
        """ returns the weight """
        return self._weight
    
    
    def __eq__(self, other):
        """ Returns true if two Term's queries are equal '"""
        return self._query == other._query
    
    
    def __lt__(self, other):
        """ Returns true if this Term's query comes before other's query """
        return self._query < other._query
    
    
    def __str__(self):
        """ Returns string containing Term's weight and query '"""
        return('%f\t%s' % (self._weight, self._query))
    
    
def build_tree(filename):
    """ Takes file with weights and queries, creates and adds Term to BST """
    infile = open(filename, 'r', encoding = 'utf-8')
    my_BST = binary_search_tree.TreeMap()                    # Create Dictionary
    infile.readline()
    for line in infile:
        line = line.strip().split('\t')                      # Split fily by tab
        temp_weight = float(line[0])
        temp_query = line[1]
        temp_term = Term(query = temp_query, weight = temp_weight)
        my_BST[temp_query] = temp_term     # Add "query(word) = object" to BST
    return my_BST                          # Return BST


def all_matches(tree, prefix):
    """ Take BST and prefix, returns Terms with prefix """
    
    term_list = []
    
    last = prefix[-1]
    num = ord(last) + 1
    end_prefix = prefix[:-1] + chr(num)               # Increase last letter of prefix to end value
    
    for i, j in tree.find_range(prefix, end_prefix):
        term_list.append(j)                           # Add keys with matching prefixes to list
        
    term_list.sort(key = Term.get_weight, reverse = True)  # Sort list greatest to least weights
    
    return term_list
    

def main():
    # User inputs
    filename = 'cities.txt' #input('Enter file: ')
    results = 5 #int(input('Enter number of results to show: '))
    prefix = input('Enter search: ')
    my_tree = build_tree(filename)
    
    while prefix != '':
        
        start = timeit.default_timer()             
        
        for i in all_matches(my_tree, prefix)[:results]:   # Cycle through only i results
            print(i)
        
        end = timeit.default_timer()
        total_time_in_ms = (end - start) * 1000            # Calculate time autocomplete took to run
        print('Query took %d ms' % total_time_in_ms)
        
        prefix = input('Enter search: ')
        
main()