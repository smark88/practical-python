# word_counter.py
'''
given an input this will count the number of occurances of a word
in text
'''
import sys
from collections import defaultdict
from collections import Counter

def openfile(filename):
    with open(filename, 'rt') as f:
        text = f.read().lower().split()
    return text

def count_vanilla(text):
    '''
    if the key is not in the dict then it need to be initialized this is why we use a "not in" statement 
    '''
    counter = {}
    for word in text:
        if word not in counter:
            counter[word] = 0
        counter[word] +=1
    return counter

def count_defaultdict(text):
    '''
    You first initialize the counter using a defaultdict with int() as a default factory function. 
    This way, when you access a key that doesn’t exist in the underlying defaultdict, the dictionary automatically 
    creates the key and initializes it with the value that the factory function returns
    '''
    counter = defaultdict(int)
    for word in text:
        counter[word] +=1
    return counter

def count_counter(text):
    '''
    Count number of words by using the built in counting function using Counter
    '''
    counter = Counter(list(text))
    return counter

def unique_count_counter(text):
    '''
    Count number unique words by using the built in counting function Counter + set
    '''
    counter = Counter(set(text))
    return counter

def main(filename):
    input = openfile(filename)
    print(count_counter(input))


if __name__ == '__main__':
    '''
    using sys can import an argument from stdin
    '''
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/sampleText.txt'
    main(filename)
