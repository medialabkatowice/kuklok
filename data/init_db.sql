DROP TABLE IF EXISTS articles;
CREATE TABLE articles(
    title          TEXT,
    source         TEXT,
    url            TEXT,
    tags           TEXT,
    date           TEXT,
    week           INTEGER,
    author         TEXT,
    districts      TEXT,
    type           TEXT,
    content_type   TEXT,
    popularity     INTEGER,
    categories     TEXT
);

DROP TABLE IF EXISTS weeks;
CREATE TABLE weeks(
    week      INTEGER,
    category  TEXT,
    city      INTEGER,
    media     INTEGER
);
