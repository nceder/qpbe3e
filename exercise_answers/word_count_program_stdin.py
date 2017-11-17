# File: word_count_program_stdin.py
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""
import sys


def main():
    # initialze counts
    line_count = 0
    word_count = 0
    char_count = 0
    filename = None
    
    option = None
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        if params[0].startswith("-"):
        # if more than one param, pop the first one as the option
            option = params.pop(0).lower().strip()
        if params:
            filename = params[0]    # open the file
    file_mode = "r"
    if option == "-c":
        file_mode = "rb"
    if filename:
        infile =  open(filename, file_mode)
    else:
        infile = sys.stdin
    with infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
    
    if option in ("-c", "-m"):
        print("File has {} characters".format(char_count))
    elif option == "-w":
        print("File has {} words".format(word_count))
    elif option == "-l":
        print("File has {} lines".format(line_count))
    else:
        # print the answers using the format() method
        print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                                       word_count, char_count))

if __name__ == '__main__':
    main()
