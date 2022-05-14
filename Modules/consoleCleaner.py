# import Module
import os

# functions declaration
def clear():
    '''Clear console'''
    if os.name in ('nt', 'dos'): 
        os.system('cls')
    else:
        os.system('clear')

# For test
if __name__ == '__main__':
    clear()