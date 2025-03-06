import requests


def fox():
    url = 'https://randomfox.ca/floof'

    response = requests.get(url)

    if response:
        return response.json().get('image')
    else:
        return 'NO'


if __name__ == '__main__':
    print(fox())