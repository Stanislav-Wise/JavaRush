# Парсер с сайта rbc.ru

# Парсер с сайта habr.ru
RBC_BASE_URL = "https://www.rbc.ru"
RBC__NEWS_URL = f"{RBC_BASE_URL}/technology_and_media/"

# RBC__CARD_SELECTOR = "article"
RBC__TITLE_SELECTOR = "a"
RBC__TITLE_LINK_SELECTOR = "item__link"  # class="item__link rm-cm-item-link js-rm-central-column-item-link "


def fetch_rbc_news_raw(limit: int = 20) -> list[dict[str, str]]:
    pass