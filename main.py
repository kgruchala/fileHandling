"""
Hi, this is my file handling program,
it will finally copy files from mem card from my camera to location G Zdjecia with folder from current year
"""
import time, os
from copy import *
from read import *

menu_options = {
    1: 'Read file you want --give full path to file',
    2: 'Copy files',
    3: 'Nothing',
    4: 'Exit',
}


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def sleep():
    time.sleep(3)


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
            time.sleep(5)
            clearConsole()
        # Check what choice was entered and act accordingly
        if option == 1:
            start_time = time.time()
            read()
            execution_time = time.time() - start_time
            print("execution time of operation was {:7.5f} ".format(execution_time))
            sleep()
            clearConsole()
        elif option == 2:
            start_time = time.time()
            copy()
            execution_time = time.time() - start_time
            print("execution time of operation was {:7.5f} ".format(execution_time))
            sleep()
            clearConsole()
        elif option == 3:
            start_time = time.time()
            print("Nothing happens here. Try out other numbers")
            execution_time = time.time() - start_time
            print("execution time of operation was {:7.5f} ".format(execution_time))
            sleep()
            clearConsole()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
            time.sleep(2)
            clearConsole()

    # read()
    # copy()
