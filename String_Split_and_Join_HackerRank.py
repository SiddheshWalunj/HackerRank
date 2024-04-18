# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
#
# Function Description
# Complete the split_and_join function in the editor below.
#
# split_and_join has the following parameters:
#
# string line: a string of space-separated words
# Returns
# string: the resulting string
# Input Format
# The one line contains a string consisting of space-separated words.
#
# Sample Input 0
# this is a string
# Sample Output 0
# this-is-a-string

def split_and_join(line):
    a = line.split(" ")
    b = "-".join(a)
    return(b)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# def split_and_join(line):
#     for i in range(0, len(line), 1):
#         if (line[i] == ' '):
#             string = line.replace(line[i], '-')
#     return string
#
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)