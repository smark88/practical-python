def permutation(string, mutation=''):
    if len(string) == 0:
        print(f'mutation {mutation}')
    for i in range(len(string)):
        
        newMutation = mutation + string[i]
        print(f'newMutation {newMutation}')
        
        newString = string[0:i] + string[i+1:]
        print(f'newString {newString}')
        
        permutation(newString, newMutation)

string1 = "ABC"
permutation(string1)