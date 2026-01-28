from pprint import pprint
import requests
from bs4 import BeautifulSoup


news_item = {
    'source': 'habr',
    'title': 'Disney разрешил Sora генерировать видео с персонажами компании и инвестирует $1 млрд в OpenAI',
    'url': 'https://habr.com/ru/companies/bothub/news/975826/',
    'published_at': '2025-12-11 18.00',
    'summary': 'Компания Disney официально разрешила пользователям Sora создавать видео с участием своих любимых персонажей без ограничений лицензий. В следующем году функция появится в Sora, и фанаты смогут генерировать материалы с героями из вселенной Disney, Pixar, Marvel и Star Wars. Disney также объявил, что лучшие работы, созданные пользователями, будут показывать подписчикам Disney+ в рамках официальных подборок и программных блоков.',
}
my_list = [news_item]

pprint(my_list)


if __name__ == '__main__':
    print('Всё хорошо')