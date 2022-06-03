# Import Module
import ftplib

# Fill Required Information >> all information from the ("https://dlptest.com/ftp-test/") website
HOSTNAME = "ftp.dlptest.com"  # >> virtual I get it from the Internet
USERNAME = "dlpuser"  # >> virtual I get it from the Internet
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"  # >> virtual I get it from the Internet

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter File Name with Extension
filename = "info.txt" # >> In the same directory

# Read file in binary mode
with open(filename, "rb") as file:
    # Command for Uploading the file "STOR filename"
    ftp_server.storbinary(f"STORE {filename}", file)

# Get list of files
ftp_server.dir()

# Close the Connection
ftp_server.quit()
