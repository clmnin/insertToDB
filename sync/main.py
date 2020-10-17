from database import connection, create_staging_table
from fetchdata import iter_beers_from_api
import oneInsertRowsOneByOne
import executeMany
import executeManyFromIterator
import executeBatch
import executeBatchFromIterator
import executeBatchFromIteratorWithPageSize
import executeValues
import executeValuesFromIterator
import executeValuesFromIteratorWithPageSize
import pgcopy
import pgcopy_csvLike
import pgcopyIterWithBuffer

print(
    "Starting to fetch the data in bulk to remove the network latency in our \
testing"
)
beers = list(iter_beers_from_api()) * 100
print("\nFinished fetching data from the API to be created into an inter\n")

with connection.cursor() as cursor:
    create_staging_table(cursor)

oneInsertRowsOneByOne.insert_one_by_one(connection, beers)

executeMany.insert_executemany(connection, beers)

executeManyFromIterator.insert_executemany_iterator(connection, beers)

executeBatch.insert_execute_batch(connection, beers)

executeBatchFromIterator.insert_execute_batch_iterator(connection, beers)

executeBatchFromIteratorWithPageSize.insert_execute_batch_iterator(
    connection, iter(beers), page_size=1
)
executeBatchFromIteratorWithPageSize.insert_execute_batch_iterator(
    connection, iter(beers), page_size=100
)
executeBatchFromIteratorWithPageSize.insert_execute_batch_iterator(
    connection, iter(beers), page_size=1000
)
executeBatchFromIteratorWithPageSize.insert_execute_batch_iterator(
    connection, iter(beers), page_size=10000
)

executeValues.insert_execute_values(connection, beers)

executeValuesFromIterator.insert_execute_values_iterator(connection, beers)

executeValuesFromIteratorWithPageSize.insert_execute_values_iterator(
    connection, iter(beers), page_size=1
)
executeValuesFromIteratorWithPageSize.insert_execute_values_iterator(
    connection, iter(beers), page_size=100
)
executeValuesFromIteratorWithPageSize.insert_execute_values_iterator(
    connection, iter(beers), page_size=1000
)
executeValuesFromIteratorWithPageSize.insert_execute_values_iterator(
    connection, iter(beers), page_size=10000
)

pgcopy.copy_stringio(connection, beers)

pgcopy_csvLike.copy_string_iterator(connection, beers)

pgcopyIterWithBuffer.copy_string_iterator(connection, iter(beers), size=1024)
pgcopyIterWithBuffer.copy_string_iterator(connection, iter(beers), size=8192)
pgcopyIterWithBuffer.copy_string_iterator(connection, iter(beers), size=16384)
pgcopyIterWithBuffer.copy_string_iterator(connection, iter(beers), size=65536)

"""
insert_one_by_one()
Time   4.899
Memory 0.08984375

insert_executemany()
Time   3.973
Memory 2.73046875

insert_executemany_iterator()
Time   4.157
Memory 0.0

insert_execute_batch()
Time   2.436
Memory 2.25

insert_execute_batch_iterator()
Time   2.421
Memory 0.0

insert_execute_batch_iterator(page_size=1)
Time   4.183
Memory 0.0

insert_execute_batch_iterator(page_size=100)
Time   2.423
Memory 0.0

insert_execute_batch_iterator(page_size=1000)
Time   2.458
Memory 0.0

insert_execute_batch_iterator(page_size=10000)
Time   2.454
Memory 0.0

insert_execute_values()
Time   1.357
Memory 5.0

insert_execute_values_iterator()
Time   1.206
Memory 0.0

insert_execute_values_iterator(page_size=1)
Time   4.11
Memory 0.0

insert_execute_values_iterator(page_size=100)
Time   1.375
Memory 0.0

insert_execute_values_iterator(page_size=1000)
Time   1.347
Memory 0.0

insert_execute_values_iterator(page_size=10000)
Time   1.411
Memory 0.0

copy_stringio()
Time   0.4516
Memory 100.39453125

copy_string_iterator()
Time   0.3283
Memory 0.0

copy_string_iterator(size=1024)
Time   0.3432
Memory 0.0

copy_string_iterator(size=8192)
Time   0.3152
Memory 0.0

copy_string_iterator(size=16384)
Time   0.302
Memory 0.0

copy_string_iterator(size=65536)
Time   0.3121
Memory 0.0

"""
