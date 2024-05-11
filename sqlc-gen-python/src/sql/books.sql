-- name: ListBookOverPrice :many
SELECT
        b.title
     ,	a.name
     ,	b.price
FROM
    books b
        LEFT JOIN
    authors a
    ON	1 = 1
        AND b.author_id = a.id
WHERE
    price > $1
ORDER BY
    b.title;
