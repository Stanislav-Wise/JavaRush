# from app.config import settings
#
#
# print(settings.debug)
# print(settings.redis_url)
# print(settings.telegram_api_id)
# print(settings.telegram_api_hash)
# print(settings.telegram_bot_token)
# print(settings.telegram_channel_id)
# print(settings.keywords_list)


# from app.tasks import ping
#
#
# r = ping.delay()
# print(r)
# print(r.id)
# print(r.get(timeout=10))


from app.tasks import collect_news


r = collect_news.delay()
print(r.id)
print(r.get(timeout=10))