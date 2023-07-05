from misskey import Misskey
from dotenv import load_dotenv
import os

from JMA import JMA
from generate_text import TextGenerator


def main():
    load_dotenv()
    HOST = os.environ["MISSKEY_INSTANCE"]
    MISSKEY_TOKEN = os.environ["MISSKEY_TOKEN"]

    mk = Misskey(HOST, MISSKEY_TOKEN)

    campus_list = [
        {
            "name": "東京千住",
            "area_code": 130000,
            "jma_link": "https://www.jma.go.jp/bosai/forecast/#area_type=class20s&area_code=1312100",
        },
        {
            "name": "埼玉鳩山",
            "area_code": 110000,
            "jma_link": "https://www.jma.go.jp/bosai/forecast/#area_type=class20s&area_code=1134800",
        },
    ]

    for campus in campus_list:
        forecast_datum = JMA(campus["area_code"])

        text = TextGenerator(
            data=forecast_datum,
            camplus_name=campus["name"],
            jma_link=campus["jma_link"],
        )

        mk.notes_create(text.generate())


if __name__ == "__main__":
    main()
