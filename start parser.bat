@echo off
chcp 65001 > nul
cls
echo ===================================
echo       TELEGRAM PARSER
echo ===================================
echo.

:: Проверка установки Telethon
echo Проверка установки библиотеки Telethon...
pip show telethon > nul 2>&1
if %errorlevel% neq 0 (
    echo Библиотека Telethon не установлена!
    echo Установка Telethon...
    pip install telethon
    if %errorlevel% neq 0 (
        echo Ошибка при установке Telethon!
        echo Пожалуйста, установите библиотеку вручную: pip install telethon
        pause
        exit /b 1
    )
    echo Библиотека Telethon успешно установлена.
) else (
    echo Библиотека Telethon уже установлена.
)

echo.
echo Проверьте настройки в файле parser.py:
echo - api_id и api_hash (получите их на my.telegram.org)
echo - chat_id (ID или username канала для парсинга)
echo.
echo Запуск парсера...
echo.

python parser.py

echo.
echo ===================================
echo Парсинг завершен! 
echo Результаты находятся в папке parse_result
echo ===================================
pause 