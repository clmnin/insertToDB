import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

SYNC_HOST = os.getenv("SYNC_HOST")
SYNC_DB = os.getenv("SYNC_DB")
SYNC_DB_USER = os.getenv("SYNC_DB_USER")
SYNC_DB_PASSWORD = os.getenv("SYNC_DB_PASSWORD")

connection = psycopg2.connect(
    host=SYNC_HOST,
    database=SYNC_DB,
    user=SYNC_DB_USER,
    password=SYNC_DB_PASSWORD,
)
connection.autocommit = True


def create_staging_table(cursor) -> None:
    cursor.execute(
        """
        DROP TABLE IF EXISTS staging_beers;
        CREATE UNLOGGED TABLE staging_beers (
            id                  INTEGER,
            name                TEXT,
            tagline             TEXT,
            first_brewed        DATE,
            description         TEXT,
            image_url           TEXT,
            abv                 DECIMAL,
            ibu                 DECIMAL,
            target_fg           DECIMAL,
            target_og           DECIMAL,
            ebc                 DECIMAL,
            srm                 DECIMAL,
            ph                  DECIMAL,
            attenuation_level   DECIMAL,
            brewers_tips        TEXT,
            contributed_by      TEXT,
            volume              INTEGER
        );
    """
    )
