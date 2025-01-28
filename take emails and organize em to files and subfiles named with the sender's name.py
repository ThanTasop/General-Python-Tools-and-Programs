import pandas as pd
import imaplib
import email
from email.header import decode_header
import os

# Email credentials
email_user = ""
email_pass = ""

# Connect to the Outlook IMAP server
try:
    imap_server = "outlook.office365.com"
    mail = imaplib.IMAP4_SSL(imap_server)
    print("Connected to the Outlook IMAP server.")
except Exception as e:
    print(f"Failed to connect to the Outlook IMAP server: {e}")
    exit()

# Log in to the email account
try:
    mail.login(email_user, email_pass)
    print("Logged in to the email account.")
except Exception as e:
    print(f"Failed to log in to the email account: {e}")
    exit()


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


df = pd.read_excel(r'C:\Users\Thanasis\Downloads\email-data.xlsx')
gb = df.groupby('Code')
codes = gb.groups

path = r'C:\Users\Thanasis\Desktop\emaildirectory'
create_folder(path)
for code, rows in codes.items():
    new_path = path + '\\' + f'{code} ({df['Address'][rows[0]]})'
    create_folder(new_path)

    name_groupby = gb.get_group(code).groupby('Name')

    for name in name_groupby.groups.keys():
        descr = ''
        for description in name_groupby.get_group(name)['Description']:
            if descr == '':
                descr += description
            else:
                descr += '-'+description

        newer_path = new_path + '\\' + f'{descr} ({name})'
        create_folder(newer_path)
        specific_sender = name_groupby.get_group(name)['FirstEMail']
        save_folder = newer_path
        try:
            mail.select("inbox")  # Change to your folder name if needed
        except Exception as e:
            print(f"Failed to select the folder: {e}")
            exit()

        # Search for all emails from the specific sender in the selected folder
        status, messages = mail.search(None, 'FROM', specific_sender)

        # Check if the search was successful
        if status == "OK":
            print(f"Search status: {status}")
            email_ids = messages[0].split()

            if email_ids:
                print(f"Found {len(email_ids)} email(s) from {specific_sender}.")
                # Loop through the email IDs and fetch the emails
                for email_id in email_ids:
                    # Fetch the email by ID
                    status, msg_data = mail.fetch(email_id, "(RFC822)")
                    print(f"Fetched email ID {email_id.decode()} with status {status}.")

                    # Get the email content
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])

                            # Decode the email subject
                            subject, encoding = decode_header(msg["Subject"])[0]
                            if isinstance(subject, bytes):
                                subject = subject.decode(encoding if encoding else "utf-8")

                            # Clean subject to use as a filename
                            clean_subject = "".join(c if c.isalnum() else "_" for c in subject)

                            # Define email filename
                            email_filename = f"{clean_subject}.eml"
                            email_path = os.path.join(save_folder, email_filename)

                            # Save the email
                            with open(email_path, "wb") as f:
                                f.write(response_part[1])

                            print(f"Email saved: {email_path}")
            else:
                print(f"No emails found from {specific_sender}.")
        else:
            print(f"Search failed with status: {status}")

# Close the connection and logout
try:
    mail.close()
    mail.logout()
    print("Closed the connection and logged out.")
except Exception as e:
    print(f"Failed to close the connection and log out: {e}")
