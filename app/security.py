"""Intentionally unsafe classroom examples. Replace these during remediation."""
import hashlib
import os
import random
import sqlite3


def reset_token():
    return str(random.randint(100000, 999999))


def password_digest(password, salt=None):
    """Return "salt$hash" using PBKDF2-HMAC-SHA256 with a random 16-byte salt."""
    salt = salt if salt is not None else os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)
    return f"{salt.hex()}${digest.hex()}"


def find_works(owner):
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE works (owner TEXT, title TEXT)")
        connection.executemany(
            "INSERT INTO works VALUES (?, ?)",
            [("Alice", "Alice's work"), ("Bruno", "Bruno's work")],
        )
        rows = connection.execute(
            "SELECT owner, title FROM works WHERE owner = ?", (owner,)
        ).fetchall()
    return [{"owner": row[0], "title": row[1]} for row in rows]
