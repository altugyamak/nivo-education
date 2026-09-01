import sqlite3
from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE_URL"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(app):
    with app.app_context():
        db = get_db()

        db.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                email TEXT,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Eski veritabanına email sütununu ekle
        columns = [
            row["name"]
            for row in db.execute("PRAGMA table_info(leads)").fetchall()
        ]

        if "email" not in columns:
            db.execute("ALTER TABLE leads ADD COLUMN email TEXT")

        db.commit()

    app.teardown_appcontext(close_db)


def lead_ekle(isim, email, telefon, mesaj=None):
    db = get_db()

    cursor = db.execute(
        """
        INSERT INTO leads (isim, email, telefon, mesaj)
        VALUES (?, ?, ?, ?)
        """,
        (isim, email, telefon, mesaj)
    )

    db.commit()
    return cursor.lastrowid


def tum_leadler():
    db = get_db()

    rows = db.execute(
        """
        SELECT id, isim, email, telefon, mesaj, tarih
        FROM leads
        ORDER BY id DESC
        """
    ).fetchall()

    return [dict(row) for row in rows]