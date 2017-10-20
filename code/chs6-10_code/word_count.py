#!/env python3.1

""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

# open the file
infile = open('word_count.tst')
# read the file and split into lines
lines = infile.read().split("\n")

# get number of lines with len() function
line_count = len(lines)
# initialize other counts
word_count = 0
char_count = 0

# iterate through the lines
for line in lines:
    # split into words
    words = line.split()
    word_count += len(words)
    # len() function returns characters when used on a string
    char_count += len(line)

# print the answers using the format() method
print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                               word_count, char_count))
    

