import uuid

import sqlalchemy
from sqlalchemy import create_engine

from sql.code import authors, books

engine = create_engine("postgresql://root:root@localhost:5432/root")


# decorator
def transaction(func):
    def wrapper():
        with engine.connect() as connection:
            try:
                connection.begin()
                func(connection)
                connection.commit()
            except Exception as e:
                connection.rollback()
                raise e

    return wrapper


class ConnectionFactory:
    @classmethod
    def get_connection(cls):
        if hasattr(cls, "engine"):
            print("engine already generated.")
        else:
            print("generate engine.")
            cls.engine = create_engine("postgresql://root:root@localhost:5432/root")
        return cls.engine.connect()


@transaction
def foo(connection: sqlalchemy.engine.Connection):
    querier = authors.Querier(conn=connection)

    id = uuid.UUID("c4b74fcb-ae5c-4270-84df-c4cb8f24d37c")
    author = querier.get_author(id=id)
    print(author)

    querier.update_author(id=id, name="author1 update", bio="bio1 update")


@transaction
def foo2(connection: sqlalchemy.engine.Connection):
    querier = authors.Querier(conn=connection)

    id = uuid.UUID("c4b74fcb-ae5c-4270-84df-c4cb8f24d37c")
    author = querier.get_author(id=id)
    print(author)

    querier.update_author(id=id, name="author1", bio="bio1")


def foo3():
    connection = ConnectionFactory.get_connection()
    with connection:
        querier = books.Querier(conn=connection)

        books_list = querier.list_book_over_price(price=100)
        print(list(books_list))


if __name__ == "__main__":
    foo()
    foo2()
    foo3()
