def concatenate_strings(string1, string2):
    return string1 + " " + string2

def slice_string(string, start, end):
    return string[start:end]

def replace_string(string, old, new):
    return string.replace(old, new)

def find_substring(string, substring):
    return string.find(substring)

def format_string(string, values):
    return string.format(*values)


def permutation(string, mutation=''):
    '''
    Find all permutations of a text field
    '''
    if len(string) == 0:
        print(mutation)
    for i in range(len(string)):
        newMutation = mutation + string[i]
        newString = string[0:i] + string[i+1:]
        permutation(newString, newMutation)

def reverse(text):
    '''
    Reverse a String
    '''
    new_text =  text[::-1]
    print(f'Using String slicing : {new_text}')

    newText = ''
    for i in text:
        newText = i + newText
    print(f'Using for loop : {newText}')

def swapNumberBuild(a,b):
    '''
    Swap two numbers without using third variable
    '''
    a, b = b, a
    print("Using in-build syntax : a is" , a , "& b is" , b)

def swapNumberMath(a,b): 
    a = a + b
    b = a - b
    a = a - b
    print("Using arithmetic operations : a is" , a , "& b is" , b)


def fib(n):
    '''
    Fibonacci sequence
    '''
    if n <= 1:
        return n
    return (fib(n-1) + fib(n-2))


def sum(n):
    '''
    Calculate the sum of all the digits in a number
    '''
    if n < 10:
        return n
    else:
        allDigits = n // 10
        lastDigit = n % 10
        return sum(allDigits) + lastDigit


def fac(n):
    '''
    Calculate the factorial of a number
    '''
    if n == 1:
        return n
    else:
        print(n)
        return (n * fac(n-1))

import os,re
def write_data(source, destination):
    '''
    Copy contents of files named like “FileA.txt, FileB.txt, …” in FolderA and FolderB to FolderC
    '''
    if not os.path.isdir(destination):
        os.mkdir(destination, 666)

    for file in os.listdir(source):
        if re.search("File.*txt", file):
            with open(source+'/'+file,'r') as f, open(destination+'/'+file,'a') as s:
                for line in f:
                    s.write(line)

# Example usage:
string1 = "Hello"
string2 = "World"
concatenated = concatenate_strings(string1, string2)
print("Concatenated:", concatenated)

string = "Hello World"
sliced = slice_string(string, 0, 5)
print("Sliced:", sliced)

replaced = replace_string(string, "Hello", "Hi")
print("Replaced:", replaced)

found = find_substring(string, "World")
print("Found:", found)

formatted = format_string("Hello, {}", ["John"])
print("Formatted:", formatted)

print("Permutations of \"" + string1 + "\" is as below,")
permutation(string1)

print('string reverse')
reverse(string1)

print('Swap two numbers without using third variable via build')
swapNumberBuild(10,20)

print('Swap two numbers without using third variable via build')
swapNumberMath(10,20)

print("Fibonacci sequence : ")
for i in range(5):
    print(fib(i))

print("Sum of digits :" , sum(2021))

print("5! (5 * 4 * 3 * 2) =", fac(5))

print('copy folder A files and copy to folder C')
write_data('FolderA','FolderC')
#
# print('copy folder B files and copy to folder C')
#
# write_data('FolderB','FolderC')