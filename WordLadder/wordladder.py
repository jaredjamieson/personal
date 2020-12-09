import lab6_queue
import stacks
import copy
""" PART 2 """
def read_dictionary(filename):
    """Reads the file containing the list of words and stores it in wordlist"""
    wordlist = dict() # This will contain all of the words
    
    infile = open(filename,'r')
    for line in infile:
        line = line.strip()
        length = len(line)                     # Loops through file and save length of word
        if length not in wordlist:             # If length doesn't exist, add to dict with value
            wordlist[length] = [line]
        else:
            wordlist[length].append(line)      # If length found, add word to values
        
    return wordlist
    
    
""" Part 3 """
def build_ladder(start, end):
    """Finds the shortest word ladder that connects start and end words.
    
    Returns None if such a ladder does not exist.
    """
    if len(start) == len(end):               # If lengths match, start word ladder
        
        wordlist = read_dictionary('dictionary.txt') # Contains all of the allowed words
        used = set() # This will be a set of words that you have used while you searched
        word_ladders = lab6_queue.Queue() # This is your queue of stacks that will hold all of the word ladders in progress
        
        used.add(start)
        
        dic_length = wordlist[len(start)]                  # Narrow dictionary to only words of length start
        for word in dic_length:
            if word not in used:                           # Check if word is already used
                differences = 0                             # Variable to check identicality between word and start
                for letter in range(len(word)):
                    if word[letter] != start[letter]:      # If indexes are identical
                        differences += 1
                if differences == 1:                        # If only one letter is identical
                    used.add(word)
                    tempstack = stacks.LinkedStack()       # Create stack and add words
                    tempstack.push(start)
                    tempstack.push(word)
                    word_ladders.enqueue(tempstack)         # Add stack to queue
                    
        while not word_ladders.is_empty():
            tempstack = word_ladders.dequeue()
            top = tempstack.top()
            #if start == "monk":
            #    print(tempstack)
            if top != end:
                for word in dic_length:
                    if word not in used:
                        differences = 0
                        for letter in range(len(word)):
                            if word[letter] != top[letter]:
                                differences += 1
                        if differences == 1:
                            used.add(word)
                            clone = copy.deepcopy(tempstack)
                            clone.push(word)
                            word_ladders.enqueue(clone)
            else:
                return tempstack
     
    else:
        return None

