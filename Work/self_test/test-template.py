def concatenate_strings(string1, string2):
'''
Output:
Concatenated: Hello World
'''
print(concatenate_strings('Hello','World'))

def slice_string(string, start, end):
'''
Output:
Sliced: Hello
'''
print(slice_string('Hello World',0,5))

def replace_string(string, old, new):
'''
Output:
Replaced: Hi World
'''
print(replace_string('Hello World','Hello','Hi'))

def find_substring(string, substring):
'''
Output:
Found: 6
'''
print(find_substring('Hello World', 'World'))

def format_string(string):
'''
Formatted: Hello, John
'''
print(format_string("Hello {World}"))

def permutation(string, mutation=''):
    '''
    Find all permutations of a text field
    '''
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
'''
Output:
Using String slicing : olleH
Using for loop : olleH
'''
print(reverse('Hello World'))

def swapNumberBuild(a,b):
    '''
    Swap two numbers without using third variable
    '''
'''
Output:
Swap two numbers without using third variable via build
Using in-build syntax : a is 20 & b is 10
'''
print(swapNumberBuild(10,20))

def swapNumberMath(a,b): 
'''
Output:
Swap two numbers without using third variable via build
Using arithmetic operations : a is 20 & b is 10
'''
print(swapNumberMath(10,20))

def fib(n):
    '''
    Fibonacci sequence, in which each number is the sum of the two preceding ones
    '''
'''
Output:
Fibonacci sequence : 
0
1
1
2
3
'''
for i in range(8):  # if no range is selected it will not show each iteration
  print(fib(i))

def sum(n):
    '''
    Calculate the sum of all the digits in a number
    '''
'''
Input: 2021
Output:
Sum of digits : 5
'''
print(f'run sum function sum', sum(2021))
#
#def fac(n):
#    '''
#    Calculate the factorial of a number
#    '''
#
#'''
#Output:
#5! (5 * 4 * 3 * 2) = 120
#'''
#
#import os,re
#def write_data(source, destination):
#    '''
#    Copy contents of files named like “FileA.txt, FileB.txt, …” in FolderA and FolderB to FolderC
#    '''
#
# print('copy folder B files and copy to folder C')
#
# write_data('FolderB','FolderC')


def maximum_product(nums):
    '''
    Calculate the maximum product of 3 distinct numbers for the array. Example 1 : for array: [5,4,1,2,6] , output — 120
    reverse sort then tke first 3 and multiple 
    '''

    '''
    This function takes an array of numbers as input, sorts the array in ascending order,
    and returns the maximum product of 3 distinct numbers. The calculation involves finding 
    the maximum product of the 3 largest numbers in the sorted array, or the product of the 2 
    smallest numbers and the largest number. The function returns the larger of these two products 
    as the final result.
    '''

print(maximum_product([5, 4, 1, 2, 6])) # Output: 120

def print_error_lines(filename):
    '''
    You are given a log file.Write code to print all the lines containing words "ERROR” and “EXCEPTION”.
    '''

print_error_lines('log.txt')