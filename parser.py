import os
import asyncio
from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

# Данные для аутентификации в API Telegram
api_id = YOUR_API_ID         # Вставьте ваш api_id (число)
api_hash = 'YOUR_API_HASH'   # Вставьте ваш api_hash (строка)

# ID или username чата/канала для парсинга
chat_id = 'YOUR_CHAT_ID_OR_USERNAME'  # Например, '@channel_name' или числовой ID

# ID пользователя для фильтрации сообщений (опционально)
filter_user_id = None  # Например, 123456789 - оставьте None, если фильтрация не нужна

# Основная папка для результатов парсинга
BASE_DIR = 'parse_result'

async def main():
    # Создаем основную папку, если её ещё нет
    os.makedirs(BASE_DIR, exist_ok=True)

    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    chat = await client.get_entity(chat_id)
    print(f"Начало парсинга чата: {getattr(chat, 'title', getattr(chat, 'username', 'Chat'))}")

    # Итерация по сообщениям чата
    async for message in client.iter_messages(chat, limit=None, from_user=filter_user_id):
        # Определяем id отправителя
        user_id = message.sender_id if message.sender_id is not None else 'unknown'
        user_dir = os.path.join(BASE_DIR, str(user_id))
        os.makedirs(user_dir, exist_ok=True)

        # Получаем информацию об отправителе
        try:
            sender = await message.get_sender()
            if sender:
                if hasattr(sender, 'username') and sender.username:
                    sender_info = f"@{sender.username}"
                elif hasattr(sender, 'first_name') and sender.first_name:
                    sender_info = f"{sender.first_name} {sender.last_name}" if hasattr(sender, 'last_name') and sender.last_name else f"{sender.first_name}"
                else:
                    sender_info = str(message.sender_id)
            else:
                sender_info = str(message.sender_id)
        except Exception as e:
            sender_info = str(message.sender_id)

        # Сохраняем текст сообщения
        text_file_path = os.path.join(user_dir, 'text.txt')
        message_text = message.text if message.text else "[Media message]"
        with open(text_file_path, "a", encoding="utf-8") as f:
            f.write(f"{message.date.isoformat()} - {sender_info} - {message_text}\n")

        # Обработка медиа-сообщений
        if message.media:
            # Фотографии
            if message.photo:
                photos_dir = os.path.join(user_dir, 'photos')
                os.makedirs(photos_dir, exist_ok=True)
                file_path = await message.download_media(file=photos_dir)
                print(f"Скачано фото: {file_path} для пользователя {user_id}")

            # Документы, аудио, видео
            elif hasattr(message, 'document') and message.document:
                downloaded = False
                for attribute in message.document.attributes:
                    # Голосовое сообщение
                    if isinstance(attribute, DocumentAttributeAudio) and getattr(attribute, 'voice', False):
                        audio_dir = os.path.join(user_dir, 'audio')
                        os.makedirs(audio_dir, exist_ok=True)
                        file_path = await message.download_media(file=audio_dir)
                        print(f"Скачано голосовое сообщение: {file_path} для пользователя {user_id}")
                        downloaded = True
                        break

                    # Видео
                    elif isinstance(attribute, DocumentAttributeVideo):
                        video_dir = os.path.join(user_dir, 'video')
                        os.makedirs(video_dir, exist_ok=True)
                        file_path = await message.download_media(file=video_dir)
                        print(f"Скачано видео: {file_path} для пользователя {user_id}")
                        downloaded = True
                        break
                # Прочие файлы
                if not downloaded:
                    files_dir = os.path.join(user_dir, 'files')
                    os.makedirs(files_dir, exist_ok=True)
                    file_path = await message.download_media(file=files_dir)
                    if file_path:
                        print(f"Скачан файл: {file_path} для пользователя {user_id}")

    await client.disconnect()
    print("Парсинг завершён.")

if __name__ == '__main__':
    asyncio.run(main())
