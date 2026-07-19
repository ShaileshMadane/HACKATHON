import base64
import os


DOWNLOAD_FOLDER = "downloads"


def download_attachment(service, message_id, attachment_id):
    attachment = service.users().messages().attachments().get(
        userId="me",
        messageId=message_id,
        id=attachment_id
    ).execute()

    file_data = base64.urlsafe_b64decode(attachment["data"])

    return file_data


def save_pdf(file_data, filename):
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    with open(file_path, "wb") as file:
        file.write(file_data)

    return file_path