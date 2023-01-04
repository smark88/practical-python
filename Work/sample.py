'''
sample of simple functions, try/except, if/elif/else and best pracitces layout
'''
def somefunction1(somevar):
    pass

def somefunction2(somevar):
    pass

def somefunction3(somevar):
    for i in range(somevar):
        try:
            if i > 0 and i < 3:
                print(i, 'greater than 0')
            elif i > 3 and i < 7:
                print(i, 'greater than 3 and less than 7')
            elif i <= 10:
                print(i, 'less than or equal to 10')
            else:
                print(i, 'numer is outside scope of 10')
        except:
            IndexError

def main():
    somefunction1('cheese') 
    somefunction2('cheese') 
    somefunction3(11)

if __name__ == '__main__':
    main()