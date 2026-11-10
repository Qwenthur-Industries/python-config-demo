# Python Config Demo

Небольшой проект показывает, как Python загружает настройки из `.env` с помощью `python-dotenv`. Скрипт выводит имя приложения и сообщает, задан ли ключ API, без вывода его значения.

## Установка

Нужен Python 3.10 или новее. В macOS или Linux выполни:

```bash
git clone https://github.com/Qwenthur-Industries/python-config-demo.git
cd python-config-demo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

В Windows для создания окружения можно использовать `py -m venv .venv`. В PowerShell активируй его командой `.venv\Scripts\Activate.ps1` и скопируй шаблон командой `Copy-Item .env.example .env`.

## Настройка и запуск

- `APP_NAME` — имя приложения, которое скрипт выводит на экран.
- `API_KEY` — обязательное значение, которое скрипт проверяет, не показывая его. Для демонстрации подходит `demo-only`. Программа никуда этот ключ не отправляет и не обращается к API.

Из папки проекта запусти `python main.py`. Со значениями из шаблона вывод будет таким:

```text
API_KEY loaded: True
APP_NAME: Python Config Demo
```

Если обязательная настройка отсутствует или пуста, скрипт подскажет, что заполнить в `.env`, и завершится с кодом 1.
