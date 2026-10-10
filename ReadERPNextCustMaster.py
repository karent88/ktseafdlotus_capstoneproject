import requests

# 1. Define your localhost URL and Endpoint
# Standard Frappe/ERPNext development port is usually 8000. Change it if your Docker setup uses a different port.
base_url = "http://localhost:8080"
endpoint = f"{base_url}/api/resource/Customer"

# 2. Format the Authorization Header
# ERPNext requires the exact word "token" followed by the Key and Secret separated by a colon
api_key = "ddb8457d95b3580"
api_secret = "0862c77931ec5b1"
headers = {
    "Authorization": f"token {api_key}:{api_secret}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# ---------------------------------------------------------
# EXAMPLE A: READ (GET) Customers
# ---------------------------------------------------------
# We use the 'fields' parameter to specify exactly which columns we want to return
params = {
    "fields": '["name", "customer_name", "customer_group", "territory"]'
}

response = requests.get(endpoint, headers=headers, params=params)

if response.status_code == 200:
    print("--- Customer List ---")
    customers = response.json().get("data", [])
    for cust in customers:
        print(f"ID: {cust.get('name')} | Name: {cust.get('customer_name')} | Group: {cust.get('customer_group')} | Territory: {cust.get('territory')}")
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")