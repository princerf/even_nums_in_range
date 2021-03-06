from __future__ import print_function
import sys , os

def print_evens():
    '''
    It's a function to do print even numbers in range input (from 0 to n , contains zero and n)
    '''

    print('You must enter a number to print even nums from 0 to that\n')
    start = 0
    inp = raw_input('> ')

    try:
        n=int(inp)
        for i in range((n/2)+1):
            print(start)
            start += 2

    except ValueError:
        print('\nYou must enter an integer')
        sys.exit(1)

    except:
        print('Something goes wrong!')

# You can use the else keyword to define a block of code to be executed if no errors were raised:
    else:
        print('*** End of the list *** / else keyword')

# The finally block, if specified, will be executed regardless if the try block raises an error or not.
    finally:
        print('\nThe program was closed / finally keyword')



# make usable for both script and module mode
if __name__ == '__main__':
    print_evens()

    print('*'*50,'\n','Enter any key to exit or enter \'h\' for HELP/README')
    inp = raw_input('> ').lower()
    if inp == 'h':
        try:
            with open('./README.md','r') as file:
                readmeFile=file.read()
                print(readmeFile)
        except IOError:
            print('\n','You should change the working directory to where files there')
        except:
            print('\n','sorry, There is not a help or readme file')
