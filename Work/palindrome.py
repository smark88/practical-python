def checker(word):
    if word is word[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    result =  checker('racecar')
    print(f'The result is {result}') 