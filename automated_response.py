import os
import smtplib
from email.message import EmailMessage

def block_ip(ip_address):
    print(f"Blocking IP: {ip_address}")
    os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")

def send_alert(ip_address):
    email_sender = "your_email@example.com"
    email_receiver = "admin@example.com"
    msg = EmailMessage()
    msg.set_content(f"ALERT: Malicious activity detected from IP {ip_address}. Action required!")
    msg["Subject"] = "Cybersecurity Alert"
    msg["From"] = email_sender
    msg["To"] = email_receiver

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(email_sender, "your_password")
        server.send_message(msg)
    
    print("Alert email sent.")


malicious_ip = "192.168.1.5"
block_ip(malicious_ip)
send_alert(malicious_ip)
