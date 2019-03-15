import requests


SITES = [
    'http://google.com',
    'http://python.org',
    'http://www.python.org/psf/',
    'http://www.packtpub.com/tech/Python'
]


def ping(url):
    res = requests.get(url)
    return res.status_code


if __name__ == '__main__':
    ping('http://p')
