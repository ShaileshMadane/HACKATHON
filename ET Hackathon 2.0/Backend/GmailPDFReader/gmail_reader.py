from base64 import urlsafe_b64decode


def get_latest_messages(service, max_results=10, query=None):
    results = service.users().messages().list(
        userId="me",
        maxResults=max_results,
        q=query
    ).execute()

    return results.get("messages", [])


def get_message(service, message_id):
    return service.users().messages().get(
        userId="me",
        id=message_id
    ).execute()


def get_header(message, header_name):
    headers = message["payload"]["headers"]

    for header in headers:
        if header["name"] == header_name:
            return header["value"]

    return None


def find_pdf_attachment(message):
    payload = message.get("payload", {})
    parts = payload.get("parts", [])

    for part in parts:
        if part.get("filename", "").lower().endswith(".pdf"):
            body = part.get("body", {})

            if "attachmentId" in body:
                return {
                    "filename": part["filename"],
                    "attachment_id": body["attachmentId"]
                }

    return None