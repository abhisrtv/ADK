import json
import requests
from google.auth import default
from google.auth.transport.requests import Request

# Get default credentials and access token
creds, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
creds.refresh(Request())
access_token = creds.token

# API endpoint for session creation
url_session = "https://xxxxxxxxxxxxxxxxxxxxxxx:query"

# Payload for session creation
payload_session = {"class_method": "create_session", "input": {"user_id": "testId"}}

# Headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# POST request
response = requests.post(url_session, headers=headers, data=json.dumps(payload_session))

if response.status_code == 200:
    data = response.json()
    session_id = data["output"]["id"]
    print(f"Session created successfully! Session ID: {session_id}")
else:
    print(f"Request failed ({response.status_code}):")
    print(response.text)

payload_query = {
    "class_method": "async_stream_query",
    "input": {
        "user_id": "testId",
        "session_id": session_id,
        "message": "What is the exchange rate from US dollars to INR today?",
    },
}

url_query = "https://xxxxxxxxxxxxxxxxx:streamQuery?alt=sse"

with requests.post(
    url_query, headers=headers, data=json.dumps(payload_query), stream=True
) as response:
    print("Status:", response.status_code)
    if response.status_code != 200:
        print("Error:", response.text)
    else:
        print("Agent Response:\n")
        for line in response.iter_lines():
            if line:
                # 1. Decode the bytes to string
                decoded_line = line.decode("utf-8")

                # 2. Convert the string to a JSON object (dictionary)
                try:
                    chunk = json.loads(decoded_line)

                    # 3. Extract the text parts only
                    # We navigate: content -> parts -> text
                    parts = chunk.get("content", {}).get("parts", [])

                    for part in parts:
                        if "text" in part:
                            # Print the text chunk immediately
                            print(part["text"], end="", flush=True)

                except json.JSONDecodeError:
                    # This skips lines that aren't valid JSON (like empty lines or SSE headers)
                    continue
        print("\n")  # Add a newline at the end
