DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS champion;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE champion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    champion_name TEXT UNIQUE NOT NULL
)