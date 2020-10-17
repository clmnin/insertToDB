from tools import profile
from typing import Iterator, Dict, Any, Optional
from utils import parse_first_brewed
from database import create_staging_table
import io
from pgcopy import clean_csv_value, copy_stringio

from StringIterator import StringIteratorIO

@profile
def copy_string_iterator(connection, beers: Iterator[Dict[str, Any]], size: int = 8192) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)
        beers_string_iterator = StringIteratorIO((
            '|'.join(map(clean_csv_value, (
                beer['id'],
                beer['name'],
                beer['tagline'],
                parse_first_brewed(beer['first_brewed']).isoformat(),
                beer['description'],
                beer['image_url'],
                beer['abv'],
                beer['ibu'],
                beer['target_fg'],
                beer['target_og'],
                beer['ebc'],
                beer['srm'],
                beer['ph'],
                beer['attenuation_level'],
                beer['brewers_tips'],
                beer['contributed_by'],
                beer['volume']['value'],
            ))) + '\n'
            for beer in beers
        ))
        cursor.copy_from(beers_string_iterator, 'staging_beers', sep='|', size=size)
