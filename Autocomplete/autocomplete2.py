# Jared Jamieson
# CS/IT 201

# Imports
import timeit, hash_tables


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
    
    
def build_map(filename):
    """ Takes file with weights and queries, creates and adds Term to ProbeHashMap """
    infile = open(filename, 'r', encoding = 'utf-8')
    my_hash = hash_tables.ProbeHashMap()                   # Create Dictionary
    infile.readline()
    for line in infile:
        line = line.strip().split('\t')                      # Split fily by tab
        temp_weight = float(line[0])
        temp_query = line[1]
        temp_term = Term(query = temp_query, weight = temp_weight)
        my_hash[temp_query] = temp_term    # For less collision, use query as index.  Class as value
        
    return my_hash                          # Return hash map


def all_matches(my_hash, prefix):
    """ Take ProbeHash and prefix, returns Terms with prefix """
    
    term_list = []
    
    for key in my_hash:               # Search through hash like dict
        if len(key) >= len(prefix):   # If len prefix is at least len of key
            if key[:len(prefix)] == prefix:  # If sliced key == prefix, add to list
                term_list.append(my_hash[key])
    
    term_list.sort(key = Term.get_weight, reverse = True)  # Sort list greatest to least weights
    
    return term_list
    

def main():
    # User inputs
    filename = 'cities.txt' #input('Enter file: ')
    results = 5 #int(input('Enter number of results to show: '))
    prefix = input('Enter search: ')
    my_hash = build_map(filename)
    
    while prefix != '':
        
        start = timeit.default_timer()             
        
        for i in all_matches(my_hash, prefix)[:results]:   # Cycle through only i results
            print(i)
        
        end = timeit.default_timer()
        total_time_in_ms = (end - start) * 1000            # Calculate time autocomplete took to run
        print('Query took %d ms' % total_time_in_ms)
        
        prefix = input('Enter search: ')
        
main()