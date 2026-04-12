# database.py

import sqlite3
from pathlib import Path

DB_PATH = Path("users.db")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                username         TEXT    UNIQUE NOT NULL,
                password         TEXT    NOT NULL,
                server_ip        TEXT    NOT NULL,
                onec_publication TEXT    NOT NULL DEFAULT 'unf_dashboard'
            )
        """)
        # Миграция: добавляем колонку в уже существующую таблицу
        columns = [row[1] for row in conn.execute("PRAGMA table_info(users)").fetchall()]
        if "onec_publication" not in columns:
            conn.execute(
                "ALTER TABLE users ADD COLUMN onec_publication TEXT NOT NULL DEFAULT 'unf_dashboard'"
            )


def get_user(username: str) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT username, password, server_ip, onec_publication FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    return dict(row) if row else None


def username_exists(username: str) -> bool:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT 1 FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    return row is not None


def create_user(username: str, password: str, server_ip: str, onec_publication: str) -> None:
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO users (username, password, server_ip, onec_publication) VALUES (?, ?, ?, ?)",
            (username, password, server_ip, onec_publication),
        )
