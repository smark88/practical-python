def cheese(filename):
    if filename is not None:
        with open(filename, 'rt') as f:
            for line in f:
                if 'ERROR' in line:
                    print(f'This is an error line \n {line}')
                elif 'EXCEPTION' in line:
                    print(f'This is an exception line \n {line}')
                else:
                    print(f'this is non line \n {line}')

if __name__ == '__main__':
    cheese('log.txt')