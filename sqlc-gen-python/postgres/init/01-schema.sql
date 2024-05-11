CREATE TABLE authors (
  id   UUID PRIMARY KEY,
  name text NOT NULL,
  bio  text
);

create table books
(
    id         UUID PRIMARY KEY,
    title      varchar(99) not null,
    price      BIGSERIAL not null,
    author_id  UUID not null,
    created_at timestamp not null default now()
);

alter table books add foreign key (author_id) references authors (id);
