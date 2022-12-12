import requests

TOTAL_NAMES = 5


def get_names(n: int) -> str:
    """ Get a random name """
    for _ in range(n):
        response = requests.get('https://api.namefake.com/')
        yield response.json()['name']


if __name__ == '__main__':
    for name in get_names(TOTAL_NAMES):
        print(name)