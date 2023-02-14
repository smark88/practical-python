





































def concatenate_strings(string1, string2):
  newString = string1 + " " + string2
  return newString
'''
Output:
Concatenated: Hello World
'''
print(concatenate_strings('Hello','World'))

def slice_string(string, start, end):
  newString = string[start:end]
  return newString
'''
Output:
Sliced: Hello
'''
print(slice_string('Hello World',0,5))

def replace_string(string, old, new):
  newString = string.replace(old,new)
  return newString
'''
Output:
Replaced: Hi World
'''
print(replace_string('Hello World','Hello','Hi'))

def find_substring(string, substring):
  newString = string.find(substring)
  return newString
'''
Output:
Found: 6
'''
print(find_substring('Hello World', 'World'))

def format_string(string):
  newString = string.format(World='John')
  return newString
'''
Formatted: Hello, John
'''
print(format_string("Hello {World}"))

import csv
def csvread()
    # opening the CSV file
    with open('Giants.csv', mode ='r')as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)

def permutation(string, mutation=''):
    '''
    Find all permutations of a text field
    '''
    if len(string) == 0:
        print(mutation)
    for i in range(len(string)):
        newMutation = mutation + string[i] 
        newString = string[0:i] + string[i+1:]
        print(newMutation)
        print(newString)
        print('------')
        '''
        first loop runs every time then recurses no more iterations other than 0, always pulls first letter out till string is 0 and prints mutation 
        A <-- newMutation pulls out (mutation + string[0]) adds to mutation
        BC <-- newString pulls out remaining String (string[0:0] + string[1:]) or ('' + 'BC')
        ------
        second recursive run
        New inputs ('BC','A')
        AB <-- newMutation pulls out B (mutation + string[1]) adds to mutation
        C <-- newString pulls out remaining String (string[0:0] + string[1:]) or ('' + 'C') 
        ------
        third recursion
        New inputs ('C','AB') 
        ABC <-- newMutation pulls out B (mutation + string[1]) adds to mutation
        '' <--- newString pulls nothing string[0:0] == '' and string[1:] == ''
        ABC <-- mutation print
        '''
        permutation(newString, newMutation)
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
    reverseSting = text[::-1]
    return reverseSting
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
    a,b = b, a
    return a,b
'''
Output:
Swap two numbers without using third variable via build
Using in-build syntax : a is 20 & b is 10
'''
print(swapNumberBuild(10,20))

def swapNumberMath(a,b): 
    total = a + b
    newA = total - a
    newB = total - b
    return newA, newB
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
    if n == 0:
      return 0
      # Check if n is 1,2
      # it will return 1
      # first two will always 0 then 1 twice
    elif n == 1 or n == 2:
      return 1
    else: # starts at 3 iteration
      return fib(n-1) + fib(n-2)
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
    # By 10 method
    # if n < 10:
    #   return n
    # else:
    #   allDigits = n // 10
    #   lastDigit = n % 10
    #   return sum(allDigits) + lastDigit
    
    # append method
    sum = 0
    for digit in str(n): 
      sum += int(digit) # loop keep appending this to previous sum 
    return sum
'''
Input: 2021
Output:
Sum of digits : 5
'''
print(f'run sum function sum', sum(2021))

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
5! (5 * 4 * 3 * 2 *1) = 120
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
#
print('copy folder A files and copy to folder C')
write_data('FolderA','FolderC')

def maximum_product(nums):
    '''
    Calculate the maximum product of 3 distinct numbers for the array. Example 1 : for array: [5,4,1,2,6] , output — 120
    reverse sort then tke first 3 and multiple 
    '''
    nums.sort(reverse=True)
    return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])
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
    with open(filename, 'r') as file:
      for line in file:
        if 'ERROR' in line or 'EXCEPTION' in line:
          print(line)

print_error_lines('log.txt')

import json
import urllib.request

def get_json_data(url):
    '''
    Make a GET request to retrieve the JSON data
    Check if the request was successful 
    '''
    response = urllib.request.urlopen(url)

    if response.getcode() == 200:
        # Load the JSON data into a Python dictionary
        return json.loads(response.read().decode())
    else:
        print("Request failed with status code:", response.getcode())
        return None

def add_item_to_json(data, new_item):
    '''
    Add a new item map item to the data top level key is array
    '''
    # if list [] append
    data.append(new_item)
    # if map {} update
    data.update({"cheese": "pizza"})
        
    return data

data = get_json_data("https://data.binance.com/api/v3/ticker/24hr")
new_item={
    "symbol": "CHEESE",
    "priceChange": "0.11900000",
    "priceChangePercent": "1.389",
    "weightedAvgPrice": "8.46937399"}

if data is not None:
    data = add_item_to_json(data, new_item)
    print(json.dumps(data, indent=4))

class Node:
    def __init__(self, data):
        """
        The constructor for the Node class.
        This function creates a new Node object and sets its data value to the input data.
        It also sets the left and right pointers to None.
        :param data: The value to store in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        The constructor for the BinaryTree class.
        This function creates a new BinaryTree object and sets its root to None.
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the input data into the binary tree.
        :param data: The value to insert into the tree.
        """
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data <= current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
bt = BinaryTree()

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

def unique_count_counter(text):
    '''
    Count number unique words by using the built in counting function Counter + set
    '''
    counter = Counter(set(text))
    return counter

def pax(time,paxlist,pax):
    '''
    scca pax outputer with dicts
    '''
    pax = pax.upper()
    if time is not None and pax in paxlist:
        try:
            output = {}
            output['Pax'] = pax
            output['Multiplier'] =  paxlist[pax]
            output['Time'] =  round(time * paxlist[pax],3)
            return output
        except:
            ValueError
            return 1

current = {
    'SS': 0.833,	 	
    'AS': 0.823,	 	
    'BS': 0.818,	 	
    }
print(pax(69.420,current,'as'))

def substringFind(string,substring):

    # Replace X with D to get the correct string
    substring.replace('X', 'D')

    # Use the index function to find the first occurrence of the substring
    index = string.index(substring)
    return index

string = 'ABCFABCXBCDABCX'
substring = 'ABCD'

print(substringFind(string,substring))  # Output: 10
