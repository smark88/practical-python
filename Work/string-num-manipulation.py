def concatenate_strings(string1, string2):
    return string1 + " " + string2

string1 = "Hello"
string2 = "World"
concatenated = concatenate_strings(string1, string2)
print("Concatenated:", concatenated)
'''
Output:
Concatenated: Hello World
'''

def slice_string(string, start, end):
    return string[start:end]

string = "Hello World"
sliced = slice_string(string, 0, 5)
print("Sliced:", sliced)
'''
Output:
Sliced: Hello
'''
def replace_string(string, old, new):
    return string.replace(old, new)

replaced = replace_string(string, "Hello", "Hi")
print("Replaced:", replaced)
'''
Output:
Replaced: Hi World
'''

def find_substring(string, substring):
    return string.find(substring)
found = find_substring(string, "World")
print("Found:", found)
'''
Output:
Found: 6
'''

def format_string(string, values):
    return string.format(*values)
formatted = format_string("Hello, {}", ["John"])
print("Formatted:", formatted)
'''
Formatted: Hello, John
'''

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
print("Permutations of \"" + string1 + "\" is as below,")
permutation('ABC')
'''
Output:
Permutations of "Hello" is as below,
ABC
ACB
BAC
BCA
CAB
CBA
'''


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
reverse(string1)
'''
Output:
Using String slicing : olleH
Using for loop : olleH
'''

def swapNumberBuild(a,b):
    '''
    Swap two numbers without using third variable
    '''
    a, b = b, a
    print("Using in-build syntax : a is" , a , "& b is" , b)
print('Swap two numbers without using third variable via build')
swapNumberBuild(10,20)
'''
Output:
Swap two numbers without using third variable via build
Using in-build syntax : a is 20 & b is 10
'''

def swapNumberMath(a,b): 
    a = a + b
    b = a - b
    a = a - b
    print("Using arithmetic operations : a is" , a , "& b is" , b)
print('Swap two numbers without using third variable via build')
swapNumberMath(10,20)
'''
Output:
Swap two numbers without using third variable via build
Using arithmetic operations : a is 20 & b is 10
'''

def fib(n):
    '''
    Fibonacci sequence
    '''
    if n <= 1:
        return n
    return (fib(n-1) + fib(n-2))
print("Fibonacci sequence : ")
for i in range(5):
    print(fib(i))
'''
Output:
Fibonacci sequence : 
0
1
1
2
3
'''

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
print("Sum of digits :" , sum(2021))
'''
Output:
Sum of digits : 5
'''

def fac(n):
    '''
    Calculate the factorial of a number
    '''
    if n == 1:
        return n
    else:
        print(n)
        return (n * fac(n-1))
print("5! (5 * 4 * 3 * 2) =", fac(5))
'''
Output:
5! (5 * 4 * 3 * 2) = 120
'''

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

print('copy folder A files and copy to folder C')
write_data('FolderA','FolderC')
#
# print('copy folder B files and copy to folder C')
#
# write_data('FolderB','FolderC')

def maximum_product(nums):
    '''
    Calculate the maximum product of 3 distinct numbers for the array. Example 1 : for array: [5,4,1,2,6] , output — 120
    '''
    nums.sort(reverse=True)
    return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])

# test the function with the example array
array = [5, 4, 1, 2, 6]
print(maximum_product(array)) # Output: 120


def print_error_lines(filename):
    '''
    You are given a log file.Write code to print all the lines containing words “errors” and “exceptions”.
    '''
    with open(filename, 'r') as file:
        for line in file:
            if 'errors' in line or 'exceptions' in line:
                print(line)

# test the function with a log file
filename = 'log.txt'
print_error_lines(filename)