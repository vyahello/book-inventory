import sqlite3

db_file = "books.db"


def create_table():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store ("
        "id INTEGER PRIMARY KEY, "
        "title TEXT, "
        "author TEXT, "
        "year INTEGER, "
        "isbn TEXT)"
    )
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM store WHERE title=? OR author=? OR year=? OR isbn=?",
        (title, author, year, isbn),
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(title, author, year, isbn):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO store VALUES (NULL, ?, ?, ?, ?)",
        (title, author, year, isbn),
    )
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(
        "UPDATE store SET title=?, author=?, year=?, isbn=? WHERE id=?",
        (title, author, year, isbn, id),
    )
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE id=?", (id,))
    conn.commit()
    conn.close()
