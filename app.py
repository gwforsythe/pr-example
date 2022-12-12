import requests


def get_name(n: int) -> str:
    """ Get a random name """
    for _ in range(n):
        response = requests.get('https://api.namefake.com/')
        if response.ok:
            yield response.json()['name']
        else:
            response.raise_for_status()


if __name__ == '__main__':
    for name in get_name(5):
        print(name)