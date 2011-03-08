# By converting each letter in a word to a number corresponding to
# its alphabetical position and adding these values we form a word
# value. For example, the word value for SKY is
# 19 + 11 + 25 = 55 = t_(10). If the word value is a triangle number
# then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K
# text file containing nearly two-thousand common English words,
# how many are triangle words?

# I've renamed words.txt as no042.txt
from math import sqrt

def is_triangular(n, hash_ = {}):
    if n in hash_:
        return hash_[n]

    # n = 1/2(x**2 + x)
    # 8n + 1 = 4x**2 + 4x + 1
    # sqrt(8n + 1) = 2x + 1
    x = int((sqrt(8*n + 1) - 1)/2)
    bool_val = (2*n == x**2 + x)
    hash_[n] = bool_val
    return bool_val

def word_to_value(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([ letters.find(letter) + 1 for letter in word ])

def num_triangle(filename):
    # Assumes file is "A","ABILITIY","ABLE",...
    fh = open(filename, "r")
    words = [ word[1:-1] for word in fh.read().split(",") ]
    fh.close()
    vals = [ word_to_value(word) for word in words ]
    triangle_hash = {}
    count = 0
    for val in vals:
        if is_triangular(val, triangle_hash):
            count += 1
    return count

if __name__ == "__main__":
    print "The answer to Euler Project, question 42 is:",
    print num_triangle("/Users/dan/Documents/sandbox/euler_project/problem_data/no042.txt")
