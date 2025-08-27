import requests

# Configuration
FLOW_ORG = "flow"
FLOW_PROJECT = "t-rcv"
BASE_URL = f"https://api.flowengineering.com/rest/v1/org/{FLOW_ORG}/project/{FLOW_PROJECT}"
REFRESH_TOKEN = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.nyA93BPVxFYkYTotLcc_5q00XopmJr-7KQkhvehHdvKuyXwzdLnXHscZdaa98rIcCu0v6L8qRafE5zDNnEBprPiub4PqvOZ7VG9QWM8XABiLSsX-V8A9DkeRbTzmzHa28taTvGzYQedwatahF16v7YkfNHJu_eVbSMIMOs7lWTXQWagw42RvXga8qwJJ5hOQKIyOVVIDEJ0_M8yXGm-A8UtRnHZEUSB0hlUPgykjM0yxV9mXDqid_OrUkTAG0Ii0BEIxqWVvI27VEl2HYnYnR6rTw2a906wEexvDPL926V_Qwa6Ar8mh5QhDgm8Qz4kpxi2IGalDNw9DHViDD_EM_g.45pbW8ovu6U4vblm.6qyw9tsMZdZMT2e35pLr8frRn-Om5Ei8dZ3q4wQry29JEl_yGqNoaF6dz-jEntuHrJwErv-Q7r606sOHLKJVl62oupYhvvhXKPBfdTP2eu8aVBqwfyJL54n-vbhaZTTCm_WrojuSa55JA2414APF4disrki0NvXda0yyeY7XL_ke-0UIulFBsRxM9DUChjjRGfQJdnBynoAEs8Bn4L4SnKPVLcfliQtFtkUiFJiR3jaZ7jSDdY6p3h0yibhHklJ3nNQJZKbXnzXFWo8c-TJA7kiLhTIMnM1kw2HSbqNiHQYp7ZJaUy4VS2np8L1SOgf8hfY9jvXwAu51RibRsyHIaDGq3NtxlbbYlwDlti3ZEk2zHS3SWtjsgFWIkngad_9RewrVILFkYA3dhTMrBRnhrSFPQ1v8Jl2kStlu47ZqR8eIsCl92YP2LtkvCfUsxcw42_fGFwBPo7gAeWsV8yfVNrlOmw4Q8clFTueugpngEuL8OELd_m9_LpB0HW6ccOgNykDfQcuYeGT5vJsLxVKPIUb9MBei6f-soQdrEKb6Y1gulXlXDfgaocFZfoGmtweH0od1pi_lScwnGGmpoVKf-yMNLvbdXYiniv4ZcEhkJqh2KXK14zW1iQQCpb2-r_E6qW0hMTBwImCDRTitL9Bfar5zpeWTRHKl-Ir7Nnz8Q6uBxiI5rTyWWQ7kpDtpLhG6Xk9FvKPePqQn3vAis2zVnaCSGIEnxjeFUQ_E6AKnyB1nW6qlB6QV0Yy_wEIi2p23df8E0ChYea-XmavtdlCltPIRKYVbB8BTi4_2fTZUdSW_C5sBd80Gn1KPO6MciEkPn5kM409Bcob8pyzEuJKXOaMz47HMhUwI8EmfLO3tg7nfjZtWH3Y9c5qZq7crZiPRwV8-0bhM1AKODQn_hLnD9VEjnPhhYOuGbuw8DSX5Zk4ODmQjut2uRPQN-b-poTcMmNsAIGfDVKHWzjnvThiZMtW0T0Djszr8xQgscm4NYq8i0ICLtJjwyiAWGWpUATGMh2jvImVkpRVUP4oYvoBiN1Syzmrqwhpuyf4bkGTcvjaSty8Q6HYn_S0mjGiKnPFJMmgdKlwX2y1evaMZcZuH4kDWoSDTpISORbwkZh0rVw63JRv05RDP5Y6m4SHjw-o7KA4PpleizLHVqxZNZ_lXMiDdw8pLhVSu8N1mqtyKIl2LwEFfu3cRoBJgdemDUaXrBESfATqapP6g6WxyNw-Hcj9mFfidAQDfbgsQWSPZBaHDRDXyhXUMzX7gFRf-HBXpV9q4cU8v55YdvXn5LLByYJnMI2SKvgxULDQYsOPs9qsohVfav0WC5yXX3w.AMpb3K5nalyQ4Cpq880GKQ"

def fetch_design_values(session):
    """Fetch the current design values from the Flow API."""
    response = session.get(f"{BASE_URL}/values/number")
    response.raise_for_status()
    return {item['id']: item['value'] for item in response.json()}

def update_flow_value(session, flow_id, value):
    """Update a Flow value using its ID."""
    response = session.put(f"{BASE_URL}/value/{flow_id}/number", json={"value": value})
    response.raise_for_status()
    print(f"Updated ID {flow_id} with value {value}.")

def get_flow_access_token(refresh_token: str) -> str:
   url = "https://api.flowengineering.com/rest/v1/auth/exchange"
   headers = {"Content-Type": "application/json"}
   response = requests.post(url, headers=headers, json={"refreshToken": refresh_token})
   response.raise_for_status()
   return response.json()["accessToken"]

# Main script logic
def main(do_update: bool = False):
    with requests.Session() as session:
        # Fetch and set the access token for auth
        access_token = get_flow_access_token(REFRESH_TOKEN)
        session.headers.update({"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"})

        # Fetch design values
        design_values = fetch_design_values(session)
        print("Fetched Flow Design Values:", design_values)

        # Extract relevant values
        target_burn_time = design_values[1]
        target_thrust = design_values[2]

        # Perform calculations
        thruster_volume = target_burn_time * target_thrust
        thruster_weight = target_max_thrust * 2

        if do_update:
            # Update calculated values back to the Flow API
            update_flow_value(session, 3, thruster_volume)

if __name__ == '__main__':
    main()
