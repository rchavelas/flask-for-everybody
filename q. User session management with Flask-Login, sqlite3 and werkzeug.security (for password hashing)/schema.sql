DROP TABLE IF EXISTS users;

CREATE TABLE users (
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);
