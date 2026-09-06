import sqlite3
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "spamguard_history.db"


def init_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS detections ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "timestamp TEXT NOT NULL, "
        "message_type TEXT NOT NULL, "
        "message TEXT NOT NULL, "
        "prediction TEXT NOT NULL, "
        "spam_probability REAL NOT NULL, "
        "safe_probability REAL NOT NULL, "
        "explanation TEXT NOT NULL)"
    )

    connection.commit()
    connection.close()


def save_detection(
    message_type,
    message,
    prediction,
    spam_probability,
    safe_probability,
    explanation
):
    init_database()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    cursor.execute(
        "INSERT INTO detections "
        "(timestamp, message_type, message, prediction, "
        "spam_probability, safe_probability, explanation) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            india_time.strftime("%Y-%m-%d %H:%M:%S"),
            message_type,
            message,
            prediction,
            spam_probability,
            safe_probability,
            " - ".join(explanation)
        )
    )

    connection.commit()
    connection.close()


def get_history():
    init_database()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, timestamp, message_type, message, prediction, "
        "spam_probability, safe_probability, explanation "
        "FROM detections ORDER BY id DESC"
    )

    rows = cursor.fetchall()
    connection.close()

    return rows