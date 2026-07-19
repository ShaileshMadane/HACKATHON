from googleapiclient.discovery import build

from auth import authenticate
from gmail_reader import (
    get_latest_messages,
    get_message,
    get_header,
    find_pdf_attachment
)
from pdf_downloader import (
    download_attachment,
    save_pdf
)
from tracker import (
    load_processed_ids,
    save_processed_id
)


def main():
    creds = authenticate()

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    query = 'subject:"ETHackathon" has:attachment filename:pdf newer_than:30d'

    messages = get_latest_messages(
        service,
        max_results=10,
        query=query
    )

    if not messages:
        print("No matching emails found.")
        return

    processed_ids = load_processed_ids()

    for message_info in messages:

        message_id = message_info["id"]

        if message_id in processed_ids:
            print(f"Skipping already processed email: {message_id}")
            continue

        message = get_message(service, message_id)

        subject = get_header(message, "Subject")
        sender = get_header(message, "From")
        date = get_header(message, "Date")

        print("\n----------------------------------")
        print(f"Subject : {subject}")
        print(f"From    : {sender}")
        print(f"Date    : {date}")

        pdf = find_pdf_attachment(message)

        if not pdf:
            print("No PDF attachment found.")
            continue

        print(f"Downloading: {pdf['filename']}")

        file_data = download_attachment(
            service,
            message_id,
            pdf["attachment_id"]
        )

        file_path = save_pdf(
            file_data,
            pdf["filename"]
        )

        print(f"Saved to: {file_path}")

        save_processed_id(message_id)
        processed_ids.add(message_id)

    print("\nDone!")


if __name__ == "__main__":
    main()
