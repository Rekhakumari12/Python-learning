

#----> Roll the die three times
#----> Generate random number in range 1...6
#----> show the die

from random import randrange
def fie():
    for die in range(1,2):

        value=randrange(1,7)
        print('+----------+')
        if value == 1:
            print('|          |')
            print('|          |')
            print('|    *     |')
            print('|          |')
            print('|          |')
        elif value == 2:
            print('|          |')
            print('|          |')
            print('|   *   *  |')
            print('|          |')
            print('|          |')
        elif value == 6:
            print('|          |')
            print('|   *   *  |')
            print('|   *   *  |')
            print('|          |')
            print('|   *   *  |')
        
        elif value == 3:
            print('|          |')
            print('| *        |')
            print('|    *     |')
            print('|        * |')
            print('|          |')
        
        elif value == 4:
            print('|          |')
            print('|   *   *  |')
            print('|          |')
            print('|   *   *  |')
            print('|          |')
        
        elif value == 5:
            print('|          |')
            print('|   *   *  |')
            print('|     *    |')
            print('|   *   *  |')
            print('|          |')

       
        else:
            ("** elligale die value..")
        print('+----------+')
        call()
def call():
    v=int(input("Roll--- press 1\nQuit---- press 2\n"))
    if v==1:
        fie()
        
    else:
        exit()

call()
