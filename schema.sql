drop table if exists links;
CREATE TABLE links(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    _destination TEXT,
    _path TEXT
)