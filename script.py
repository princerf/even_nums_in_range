from __future__ import print_function

def print_evens():
    '''
    It's a function to do print even numbers in range input (from 0 to n , contains zero and n)
    '''

    print('You must enter a number to print even nums from 0 to that\n')
    n = int(raw_input('> '))
    start = 0

    for i in range((n/2)+1):
        print(start)
        start += 2


# make usable for both script and module mode
if __name__ == '__main__':
    print_evens()
