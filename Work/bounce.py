# bounce.py
#
# Exercise 1.5
'''
A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table 
showing the height of the first 10 bounces.
'''
def main():
    height = 100
    drop = 3/5

    for i in range(10):
        height = height * drop
        #height = round(height, 4)
        #print(i, height)
        print(i, round(height, 2))

if __name__ == '__main__':
    main()