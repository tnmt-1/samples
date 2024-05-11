# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.25.0
# source: authors.sql
from typing import Iterator, Optional
import uuid

import sqlalchemy

from sql.code import models


CREATE_AUTHOR = """-- name: create_author \\:one
INSERT INTO authors (
  id, name, bio
) VALUES (
  :p1, :p2, :p3
)
RETURNING id, name, bio
"""


DELETE_AUTHOR = """-- name: delete_author \\:exec
DELETE FROM authors
WHERE id = :p1
"""


GET_AUTHOR = """-- name: get_author \\:one
SELECT id, name, bio FROM authors
WHERE id = :p1 LIMIT 1
"""


LIST_AUTHORS = """-- name: list_authors \\:many
SELECT id, name, bio FROM authors
ORDER BY name
"""


UPDATE_AUTHOR = """-- name: update_author \\:exec
UPDATE authors
  set name = :p2,
  bio = :p3
WHERE id = :p1
"""


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def create_author(self, *, id: uuid.UUID, name: str, bio: Optional[str]) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(CREATE_AUTHOR), {"p1": id, "p2": name, "p3": bio}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    def delete_author(self, *, id: uuid.UUID) -> None:
        self._conn.execute(sqlalchemy.text(DELETE_AUTHOR), {"p1": id})

    def get_author(self, *, id: uuid.UUID) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(GET_AUTHOR), {"p1": id}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    def list_authors(self) -> Iterator[models.Author]:
        result = self._conn.execute(sqlalchemy.text(LIST_AUTHORS))
        for row in result:
            yield models.Author(
                id=row[0],
                name=row[1],
                bio=row[2],
            )

    def update_author(self, *, id: uuid.UUID, name: str, bio: Optional[str]) -> None:
        self._conn.execute(sqlalchemy.text(UPDATE_AUTHOR), {"p1": id, "p2": name, "p3": bio})
