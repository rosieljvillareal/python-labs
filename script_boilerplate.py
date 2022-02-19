import random
from time import sleep

def err_handler():
    try:
        # This is the main code
        name = 'rose'
        age = 23
    
    except TypeError as e:
        raise e
    except NameError as e:
        raise e    
    except (IndexError, ImportError) as e:
        # Handle multiple errors
        raise e
    except Exception as e:
        raise e
        # Use Exception as a catch-all
        # This block will execute if an error occurs
        # Note: variables declared in try block will
        # not exist here, esp. where exception happens
        
        # breakpoint() # Use name, dir(), locals()
        
    else:
        # This block will execute when no exception occurs
        msg = f'Hello {name}, you are {age} years old.'
        print(msg)
        
    finally:
        # This block will execute whether the code fails or not
        # Use this to do any cleanup wheny an exception occurs
        print('Done.')

def infinite_loop():
    while True: # Exit using Ctrl + C
        try:
            print("Just keep looping...")
            pause = random.randint(0,3)
            print(f'pausing for {pause}s')
            sleep(pause)
        except KeyboardInterrupt:
            break
    print('Done!')

def main(xargs):
    breakpoint()
    if xargs.infinite:
        infinite_loop()
    else:    
        err_handler()

if __name__ == '__main__':
    # Code placed here will only run when this module
    # is run from the command line
    import argparse
    parser = argparse.ArgumentParser()
    
    # flag argument becomes a property of Namespace object (xargs) once parse_args() run
    parser.add_argument('--infinite', '-I', 
    help='Call the infinite loop func',
    action='store_true')
    
    # Add arguments here
    xargs = parser.parse_args()
    main(xargs)
    
