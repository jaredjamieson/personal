import wordladder
""" DO NOT CHANGE """
def main():
    infile = None
    try:
        infile = open('input.txt','r')
        for line in infile:
            pieces = line.split()
            start = pieces[0]
            end = pieces[1]
            
            ladder = wordladder.build_ladder(start, end)
            
            if ladder is None:
                print('There is no word ladder between '+start+' and '+end+'!')
            else:
                print(ladder)
                
    except IOError:
        print('Wrong file name!')
    
    finally:
        if infile is not None:
            infile.close()
main()