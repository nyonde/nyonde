import socket
import smtplib
from email.mime.text import MIMEText

# Define the target host and ports to scan
target_host = "192.168.43.1"  # Replace with the target IP or hostname
ports_to_check = [80, 443, 22, 3389]  # Ports to check

def is_port_open(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def notify_admin(open_ports):
    admin_email = "22ports@example.com"  # Replace with the admin's email
    message = f"Open ports detected on {target_host}: {open_ports}"

    msg = MIMEText(message)
    msg["Subject"] = "Security Alert: Open Ports Detected"
    msg["From"] = "security@example.com"  # Replace with a valid email address
    msg["To"] = admin_email

    smtp_server = "smtp.example.com"  # Replace with the SMTP server
    smtp_port = 587  # Replace with the SMTP port

    smtp_username = "your_username"
    smtp_password = "your_password"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg["From"], msg["To"], msg.as_string())

if __name__ == "__main__":
    open_ports = [port for port in ports_to_check if is_port_open(target_host, port)]

    if open_ports:
        print(f"Open ports detected on {target_host}: {open_ports}")
        notify_admin(open_ports)
    else:
        print(f"No open ports found on {target_host}")
