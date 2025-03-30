# Telegram Parser

## Описание
Этот инструмент предназначен для загрузки сообщений и медиафайлов из Telegram каналов/чатов с помощью официального API Telegram. Парсер позволяет скачивать контент даже в случаях, когда в канале отключена возможность ручного сохранения медиафайлов.

## Description
This tool is designed to download messages and media files from Telegram channels/chats using the official Telegram API. The parser allows you to download content even when manual saving of media files is disabled in the channel.

## Функциональные возможности
- Загрузка всех текстовых сообщений из указанного канала/чата
- Сохранение медиафайлов различных типов:
  - Фотографии
  - Видео
  - Голосовые сообщения
  - Документы и другие файлы
- Организация контента по ID отправителей
- Возможность фильтрации сообщений по конкретному пользователю

## Features
- Download all text messages from a specified channel/chat
- Save various types of media files:
  - Photos
  - Videos
  - Voice messages
  - Documents and other files
- Organization of content by sender IDs
- Ability to filter messages by a specific user

## Настройка и использование

### Требования
- Python 3.6+
- Библиотека Telethon (`pip install telethon`)

## Setup and Usage

### Requirements
- Python 3.6+
- Telethon library (`pip install telethon`)

### Начало работы
1. Получите `api_id` и `api_hash` на сайте [my.telegram.org](https://my.telegram.org)
2. Откройте файл `parser.py` и замените следующие параметры:
   - `api_id` - ваш API ID (числовое значение)
   - `api_hash` - ваш API Hash (строка)
   - `chat_id` - ID или username канала/чата для парсинга (например, '@channel_name' или числовой ID)
   - `filter_user_id` - опционально укажите ID пользователя для фильтрации сообщений (или оставьте None)

### Getting Started
1. Get your `api_id` and `api_hash` at [my.telegram.org](https://my.telegram.org)
2. Open the `parser.py` file and replace the following parameters:
   - `api_id` - your API ID (numeric value)
   - `api_hash` - your API Hash (string)
   - `chat_id` - ID or username of the channel/chat to parse (e.g., '@channel_name' or numeric ID)
   - `filter_user_id` - optionally specify a user ID for message filtering (or leave as None)

### Запуск
Есть два способа запуска:
1. Запустить файл `start parser.bat` (Windows)
2. Выполнить команду в консоли:
```
python parser.py
```

После запуска скрипт создаст папку `parse_result` и начнёт загрузку всех сообщений и медиафайлов.

### Running
There are two ways to run the parser:
1. Run the `start parser.bat` file (Windows)
2. Execute the command in the console:
```
python parser.py
```

After starting, the script will create a `parse_result` folder and begin downloading all messages and media files.

## Структура результатов
```
parse_result/
├── [user_id_1]/
│   ├── text.txt
│   ├── photos/
│   ├── video/
│   ├── audio/
│   └── files/
├── [user_id_2]/
│   └── ...
└── ...
```

## Results Structure
```
parse_result/
├── [user_id_1]/
│   ├── text.txt
│   ├── photos/
│   ├── video/
│   ├── audio/
│   └── files/
├── [user_id_2]/
│   └── ...
└── ...
```

## ⚠️ Предупреждение
**Данный инструмент создан исключительно в образовательных целях!**

Использование этого инструмента может противоречить:
- Условиям использования Telegram
- Правилам конкретных каналов/чатов
- Законам об авторском праве и интеллектуальной собственности

**Разработчик не несёт ответственности за:**
- Заблокированные аккаунты Telegram
- Юридические последствия неправомерного использования скрипта
- Любые другие проблемы, возникшие в результате использования данного инструмента

Вы используете этот скрипт на свой страх и риск.

## ⚠️ Warning
**This tool is created for educational purposes only!**

Using this tool may contradict:
- Telegram's Terms of Service
- Rules of specific channels/chats
- Copyright and intellectual property laws

**The developer is not responsible for:**
- Blocked Telegram accounts
- Legal consequences of misuse of the script
- Any other problems arising from the use of this tool

You use this script at your own risk. 