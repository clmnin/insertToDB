# Experiments to measure DB inserts

These little scripts are to help me gauge the performances of differnet DB adapters and ORMs. 

## Synchronous

We've been writing synchronously for ages. And our approaches to do more at once has made languages give us threads and multiprocessing. Which are independent `pthread` like threads minding their own businesses. But with every thing fun there are caveats. Theres are infamous for having race conditions and a hard task for "any" engineer to take care of. It requires a lot of care.

Here we'll use a few synchronous adaptors and ORMs to gauge the speed to insert data into the database.

### psycopg2

From Haki Benita's [blog post](https://hakibenita.com/fast-load-data-python-postgresql)

## TODO

- [x] psycopg2
- [ ] SQLAlchemy 1.3
- [ ] asyncpg
- [ ] Gino
- [ ] SQLAlchemy 1.4
- [ ] EdgeDB
