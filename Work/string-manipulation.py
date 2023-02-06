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
