# -*- coding: utf-8 -*-



def has_no_e(word):
    return not 'e' in word
    
def show_no_e():
    fin = open('words.txt')
    num = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print word
            num = num + 1
    fin.seek(0)
    all_num = len(fin.readlines())
    print num,all_num
    print 'the percent is', 1.0 * num / all_num
    
def avoids(string):
    string = raw_input("input avoid string:")
    for letter in string:
        if letter in word:
            return False
    return True

#show_no_e()
#print avoids('abcde','fghi')
#fin = open('words.txt')

a = 1
def fun():
    a = 2
    print a

fun()
print a

