from linked_binary_tree import *
from binary_tree import BinaryTree

class MyTree(LinkedBinaryTree):
    def __init__(self):
        super().__init__()
        self._add_root('Does it have legs?')
        self._position = self.root()                         # Start at the top of the tree, change as traverse through tree
        self._add_left(self._position, 'Cat')
        self._add_right(self._position, 'Snake')


def play_game():
    """ Guesses an animal in 20 questions or less """
    
    
    def response(answer):
        """ Returns the user's response simplified"""
        if answer in ['YES', 'Yes', 'y', 'Y', 'yes']:
            return 'yes'
        elif answer in ['NO', 'no', 'N', 'n', 'No']:
            return 'no'
        else:
            raise ValueError('Invalid response')
        
    
    """ Load previous game or start new game """
    new_game = input('Load previous game? ')
    mytree = None                                                          # Prime variable for current tree settings
    
    
    if response(new_game) == 'yes':
        new_game = input('Enter name of file: ')                           # Load a previously existing tree
        mytree = MyTree.load_tree(new_game)
    elif response(new_game) == 'no':
        mytree = MyTree()                                                  # Create a new tree
        
        
    def change_position(change):
        """ Changes current position in Tree : Change = Left or Right"""
        if response(change) == 'yes':
            mytree._position = mytree.left(mytree._position)               # If answer is yes, move left
            return mytree._position
        elif response(change) == 'no':
            mytree._position = mytree.right(mytree._position)              # If answer is no, move right
            return mytree._position
        else:
            raise NameError('Response not recognized')                     # If answer cannot be read in response(), NameError
    
    
    def at_end():
        """ Checks if position is at end of the tree """
        return mytree.num_children(mytree._position)
    
    """ Start Game """
    user_continue = 'yes'
    while response(user_continue) == 'yes':
        print('\nThink of an animal, and I will guess it.')                # Print first computer's statement
        while at_end() != 0:                                               # Check if current position has leaves
            temp_answer = input(mytree._position.element() + ' ')          # Print question and ask for a yes or no
            change_position(response(temp_answer))                         # Move position

            
        temp_answer = input('Is it a %s ' %(mytree._position.element() + '?'))  # Make a guess
        if response(temp_answer) == 'yes':
            user_continue = input('I win!  Continue? ')                    # Condition if final guess is right
            
        elif response(temp_answer) == 'no':
            new_animal = input('I give up.  What is it? ')                 # Condition if final guess is wrong
            new_question = input('Please type a question whose answer is yes for %s and no for %s.\n' % (new_animal, mytree._position.element()))
            wrong_guess = mytree._position.element()
            mytree._replace(mytree._position, new_question)                # Replace wrong guess with question
            mytree._add_left(mytree._position, new_animal)                 # Add input animal to 'yes' leaf
            mytree._add_right(mytree._position, wrong_guess)               # Add old animal to 'no' leaf
            user_continue = input('Continue?  ')                           # Ask to play again
             
        mytree._position = mytree.root()                                   # Reset position to top (root)
        
    if response(user_continue) == 'no':
        save = input('Would you like to save your tree? ')                # Ask to save build tree
        if response(save) == 'yes':
            filename = input('Enter file saveas: ')  
            mytree.save_tree(filename)                                    # Save file to user filename
    
    print('\nGood-bye')

play_game()