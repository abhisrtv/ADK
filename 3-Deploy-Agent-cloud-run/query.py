import requests
import json


def call_agent(prompt):
    base_url = "https://clourunagentxxxxxxxxxxxxx.run.app"
    app_name = "firstAgent"  # to check app name use - https://clourunagentxxxxxxxxxxx.us-central1.run.app/list-apps
    user_id = "user_1234"
    session_id = "session_1234"

    # --- STEP 1: Initialize the Session ---
    # ADK expects a POST to /apps/{app}/users/{user}/sessions/{session}
    init_url = f"{base_url}/apps/{app_name}/users/{user_id}/sessions/{session_id}"

    print(f"Initializing session at: {init_url}")
    # We send an empty JSON object to create the session
    init_resp = requests.post(init_url, json={})

    if init_resp.status_code not in [200, 201]:
        print(f"Session init failed: {init_resp.text}")
        return

    # --- STEP 2: Run the Query ---
    run_url = f"{base_url}/run"
    payload = {
        "appName": app_name,
        "userId": user_id,
        "sessionId": session_id,
        "newMessage": {"role": "user", "parts": [{"text": prompt}]},
    }

    try:
        print(f"Sending query to agent...")
        response = requests.post(run_url, json=payload)
        response.raise_for_status()

        # ADK returns a list of events. We look for the final text response.
        events = response.json()
        for event in events:
            if "content" in event:
                for part in event["content"].get("parts", []):
                    if "text" in part:
                        print(f"\nAgent: {part['text']}")

    except Exception as e:
        print(f"Error during execution: {e}")


if __name__ == "__main__":
    call_agent("what is exchange rate from USD to INR?")
