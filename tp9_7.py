# -*- coding: utf-8 -*-
"""
thinkpython chapter 10
"""
def same(word):
    if len(word) < 6:
        return False
    i = 0
    while i+5 <= len(word)-1:
        if word[i]== word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True
        i = i+1
    return False

def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if same(word):
            print word


print 'Here are all the words in the list that have'
print 'three consecutive double letters.'
find_triple_double()
print ''