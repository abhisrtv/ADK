# Deploy ADK Agent to Google Cloud Run

This guide walks through deploying an ADK agent to **Google Cloud Run** using the `adk` CLI.

---

## Step 1: Create `requirements.txt`

Create a file named `requirements.txt` with the following content:

```txt
google-cloud-aiplatform[agent_engines,adk]>=1.112
```

---

## Step 2: Enable Cloud Build API

Make sure the **Cloud Build API** is enabled for your project.

You can enable it from the Google Cloud Console:
- APIs & Services → Library → Cloud Build API → Enable

---

## Step 3: Deploy to Cloud Run (CLI)

### Syntax
```bash
adk deploy cloud_run --project=[project] --region=[region] path/to/my_agent
```

### Example Command
```bash
adk deploy cloud_run   --project=project-xxxxxxxxx   --region=us-central1   --service_name=clourunagent1   firstAgent
```

**Note:**  
Align your terminal to the **parent directory** of `firstAgent`.

Example:
```text
(adk) D:\Current learning\adk-deploy-cloudrun\testAgent>
```

---

## Step 4: Access the Deployed Agent from Terminal

Copy the deployed URL from Cloud Run and run:

```bash
curl -X GET https://xxxxxxxxxxxxxxxx.us-central1.run.app/list-apps
```

---

## Step 5: Deploy with UI Enabled on Cloud Run

To deploy the agent with a UI:

```bash
adk deploy cloud_run   --project=project-xxxxxxxxxxxxx   --region=us-central1   --service_name=clourunagent1   --with_ui   firstAgent
```

---

✅ Your ADK agent should now be live on Cloud Run.
