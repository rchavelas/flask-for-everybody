DROP TABLE IF EXISTS users;

CREATE TABLE users (
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);


