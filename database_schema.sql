CREATE DATABASE IF NOT EXISTS gamematch
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE gamematch;

CREATE TABLE IF NOT EXISTS games (
    id VARCHAR(80) PRIMARY KEY,
    name VARCHAR(160) NOT NULL,
    genre VARCHAR(60) NOT NULL,
    platform VARCHAR(60) NOT NULL,
    mode VARCHAR(60) NOT NULL,
    difficulty VARCHAR(60) NOT NULL,
    duration VARCHAR(60) NOT NULL,
    mood VARCHAR(60) NOT NULL,
    image TEXT NOT NULL,
    tags JSON NOT NULL
);
