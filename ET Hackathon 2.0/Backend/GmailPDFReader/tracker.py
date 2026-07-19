import os

TRACKER_FILE = "processed_emails.txt"


def load_processed_ids():
    if not os.path.exists(TRACKER_FILE):
        return set()

    with open(TRACKER_FILE, "r") as file:
        return set(line.strip() for line in file if line.strip())


def save_processed_id(message_id):
    with open(TRACKER_FILE, "a") as file:
        file.write(f"{message_id}\n")