from typing import Iterator, Dict, Any
from urllib.parse import urlencode
import requests


def iter_beers_from_api(page_size: int = 5) -> Iterator[Dict[str, Any]]:
    session = requests.Session()
    page = 1
    while True:
        response = session.get('https://api.punkapi.com/v2/beers?' + urlencode({
            'page': page,
            'per_page': page_size
        }))
        response.raise_for_status()

        data = response.json()
        if not data:
            break

        yield from data

        page += 1
