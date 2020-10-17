from database import connection, create_staging_table
from fetchdata import iter_beers_from_api
import oneInsertRowsOneByOne

print(
    "Starting to fetch the data in bulk to remove the network latency in our \
testing"
)
beers = list(iter_beers_from_api()) * 100
print("\nFinished fetching data from the API to be created into an inter\n")

with connection.cursor() as cursor:
    create_staging_table(cursor)

oneInsertRowsOneByOne.insert_one_by_one(connection, beers)