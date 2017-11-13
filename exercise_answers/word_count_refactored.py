#!/env python3

""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

# initialze counts
line_count = 0
word_count = 0
char_count = 0

# open the file
with  open('word_count.tst') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)

# print the answers using the format() method
print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                               word_count, char_count))
    

