# Q1. Write a program that reads in all the lines of the file
# (take any random or article from wikipedia), and then create a dictionary,
# where the key is the line number and value is another dictionary.
# This another dictionary should contain length of the words as keys,
# and the number of words having same length as values.


# Example, first line in the file: "The quick brown fox jumps over the lazy dog"

# output - {
#     1: {
#     		3: 4  # This is comment for explaination. There are four words having 3 chars - the, fox, the, dog
#     		5: 3  # This is comment for explaination. There are 3 words having 5 chars - quick, brown, jumps
#     		4: 2  # This is comment for explaination. There are 2 words having 4 chars - over, lazy
#     	}
#     }


def words_length(filename):
    file = open(filename, 'r')
    output = {}
    for lineno, line in enumerate(file):
        wordcount = {}
        for word in line.split():
            key = len(word)
            if key not in wordcount:
                wordcount[key] = 1
            else:
                wordcount[key] += 1
        output[lineno+1] = wordcount
    return output


print(words_length("task1.txt"))
