import os
from pathlib import Path

from dotenv import load_dotenv


def main() -> int:
    load_dotenv(Path(__file__).with_name(".env"))
    app_name = os.getenv("APP_NAME", "").strip()
    has_api_key = bool(os.getenv("API_KEY", "").strip())

    print(f"API_KEY loaded: {has_api_key}")
    if not app_name or not has_api_key:
        print("Заполни APP_NAME и API_KEY в файле .env.")
        return 1

    print(f"APP_NAME: {app_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
