import os
import requests

# ==========================
# 1. Simulated SQL Injection
# ==========================
def simulate_sql_injection():
    print("\n=== Testing SQL Injection ===")
    user_input = "'; DROP TABLE users; --"
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    print("Generated Query:", query)

# ==========================
# 2. Simulated XSS Attack
# ==========================
def simulate_xss_attack():
    print("\n=== Testing Cross-Site Scripting (XSS) ===")
    user_input = "<script>alert('XSS Attack!');</script>"
    html_output = f"<div>{user_input}</div>"
    print("Generated HTML:", html_output)

# ==========================
# 3. Simulated Command Injection
# ==========================
def simulate_command_injection():
    print("\n=== Testing Command Injection ===")
    user_input = "&& rm -rf /"  # Dangerous command (simulated, not executed)
    command = f"ls {user_input}"
    print("Generated Command:", command)
    # Note: This is just a simulation; do NOT execute the command.

# ==========================
# 4. Simulated Phishing Email
# ==========================
def simulate_phishing_email():
    print("\n=== Testing Phishing Email ===")
    email_subject = "Urgent: Verify Your Account"
    email_body = """
    Dear User,

    We have detected unusual activity on your account. Please verify your details immediately by clicking the link below:

    http://malicious-site.com/verify?token=12345

    Thank you,
    Your Bank
    """
    print("Email Subject:", email_subject)
    print("Email Body:", email_body)

# ==========================
# 5. Simulated Brute-Force Login
# ==========================
def simulate_brute_force_login():
    print("\n=== Testing Brute-Force Login ===")
    username = "admin"
    password_list = ["password123", "admin123", "letmein", "qwerty"]
    for password in password_list:
        print(f"Trying username: {username}, password: {password}")
        # Simulate login attempt (no actual login performed)

# ==========================
# 6. Simulated File Upload Vulnerability
# ==========================
def simulate_file_upload_vulnerability():
    print("\n=== Testing File Upload Vulnerability ===")
    file_name = "exploit.exe"
    file_content = b"\x90\x90\xEB\xFE"  # Simulated binary content