from urllib.request import urlopen


def get(url):
    with urlopen(url) as response:
        for line in response:
            line = line.decode()             # Convert bytes to a str
            print(line)
            #if line.startswith('datetime'):

if __name__ == '__main__':
    get('http://sololive.ner.org/results_live.htm')
    # get('http://worldtimeapi.org/api/timezone/etc/UTC.txt')