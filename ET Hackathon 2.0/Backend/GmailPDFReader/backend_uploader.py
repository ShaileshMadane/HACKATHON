print("Loaded backend_uploader from:", __file__)
import requests
import os
from config import BACKEND_URL, TIMEOUT


def upload_pdf(file_path, token=None):
    headers = {}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    with open(file_path, "rb") as f:
        files = {
            "files": (
                os.path.basename(file_path),
                f,
                "application/pdf"
            )
        }

        response = requests.post(
            BACKEND_URL,
            headers=headers,
            files=files,
            timeout=TIMEOUT
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()