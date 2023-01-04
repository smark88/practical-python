def checker(word):
    if word == word[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    checker('fuckshit')