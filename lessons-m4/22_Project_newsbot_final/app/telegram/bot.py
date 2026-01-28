from pathlib import Path
import logging
from telethon import TelegramClient
from app.config import settings


logger = logging.getLogger(__name__)

SESSION_DIR = Path('data') / 'telegram'
SESSION_NAME = 'bot_session'


def _ensure_session_dir() -> None:
    SESSION_DIR.mkdir(parents=True, exist_ok=True)


async def get_telegram_client() -> TelegramClient:
    _ensure_session_dir()

    session_path = str(SESSION_DIR / SESSION_NAME)

    client = TelegramClient(
        session=session_path,
        api_id=settings.telegram_api_id,
        api_hash=settings.telegram_api_hash
    )

    try:
        await client.start(bot_token=settings.telegram_bot_token)
        logger.info(f"Telegram client started session={session_path}")
        return client
    except Exception as e:
        logger.exception(f"Telegram client failed session={session_path}")
        raise


if __name__ == '__main__':
    import asyncio


    async def main() -> None:
        client = await get_telegram_client()
        me = await client.get_me()
        print(f'Подключился как id={me.id}, username={me.username}')
        await client.disconnect()


    asyncio.run(main())
