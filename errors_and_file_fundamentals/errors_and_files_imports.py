# %%
import pathlib
## Types of Modes for opening a file
# r for reading – The file pointer is placed at the beginning of the file. This is the default mode.
# r+ Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
# w Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# rb Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
# rb+ Opens a file for both reading and writing in binary format.
# wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# a Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# ab Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# a+ Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# x open for exclusive creation, failing if the file already exists (Python 3)


def open_file(file_name):
    try: # will first try everything within the 'try'
        # file = open(file_name, 'r') # opens the file called 'order.txt' in current directory.
        # file_lines = file.readlines() # The readlines() method returns a list containing each line in the file as a list item.
        # for line in file_lines: # the for loop is removing the '\n' from the text which usually represents a new line.
        #     print(line.rstrip('\n')) # prints the text in the file
        # file.close() # closes the files once completed everything we wanted to do with it
    
        # does the same thing as the above set of code
        with open(file_name, 'r') as file: # this will open and close the file once everything within the 'with' statement is done.
            for line in file.readlines():
                print(line.rstrip('\n'))
    
    except FileNotFoundError as errmsg: # performs everything within this clause if a 'FileNotFoundError' occurs
        print('File not found! waduheck >:|', errmsg) # returns the message we gave and the original error message
        raise # returns the full technical error message with all the red text etc

open_file(f'{pathlib.Path("order.txt").parent.resolve()}\errors_and_file_fundamentals\order.txt')
# %%
