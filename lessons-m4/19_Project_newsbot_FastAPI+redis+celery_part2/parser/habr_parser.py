import requests
from bs4 import BeautifulSoup
from pathlib import Path


def parse_habr_list_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    news_items: list[dict] = []

    # article_tags = soup.select("article.tm-article-list__item")
    article_tags = soup.select("article")
    # print('*' * 50)
    # print(article_tags)
    # print('*' * 50)
    for article_tag in article_tags:
        title_link = article_tag.find('a', class_="tm-title__link")
        if title_link is None:
            continue

        title_text = title_link.get_text(strip=True)
        relative_url = title_link.get('href', '')
        if relative_url is None:
            continue

        if relative_url.startswith("http"):
            full_url = relative_url
        else:
            full_url = f'https://habr.com{relative_url}'

        news_item = {
            'source': 'habr',
            'title': title_text,
            'url': full_url,
        }
        news_items.append(news_item)

    return news_items


if __name__ == '__main__':
    html_path = Path('./data/raw_html/habr_news_list.html')
    html_text = html_path.read_text(encoding='utf-8')
    news = parse_habr_list_html(html_text)
    # print(news)
    print(f'Всего новостей {len(news)}')
    for news_item in news[:10]:
        print(f"{news_item.get('title')} -> {news_item.get('url')}")
    print(' HABR - Всё хорошо')
