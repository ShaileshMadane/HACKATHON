# Gmail PDF Reader

This project downloads PDF attachments from a shared Gmail account.

## Features

- Gmail OAuth Authentication
- Search emails using Gmail queries
- Download PDF attachments
- Prevent duplicate downloads
- Modular code structure

## Project Structure

```
GmailPDFReader/
│
├── auth.py
├── gmail_reader.py
├── pdf_downloader.py
├── tracker.py
├── main.py
│
├── credentials.json
├── token.json
│
├── downloads/
├── processed_emails.txt
│
├── requirements.txt
└── .gitignore
```

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Gmail Query

```python
query = 'subject:"[ETHackathon]" has:attachment filename:pdf'
```

Only emails matching this query will be processed.

Downloaded PDFs are stored inside the `downloads/` folder.

Processed emails are tracked in `processed_emails.txt`.