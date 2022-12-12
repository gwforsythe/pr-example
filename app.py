import requests

TOTAL_NAMES = 5

def get_name(n: int) -> str:
    """ Get a random name """
    for _ in range(n):
        response = requests.get('https://api.namefake.com/')
        yield response.json()['name']


if __name__ == '__main__':
    for name in get_name(TOTAL_NAMES):
        print(name)