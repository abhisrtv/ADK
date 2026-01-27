# 🚀 Google ADK – Setup & Run Guide  
Cloud Shell & VS Code (Google AI + Vertex AI)

---

## ☁️ Google Cloud Shell – Google AI Backend

### Step 1: Create Working Directory
```bash
mkdir adk
cd adk
```

### Step 2: Install Google ADK
```bash
pip install google-adk
pip show google-adk
```

### Step 3: Create Agent Workspace
```bash
mkdir test-agent
cd test-agent
```

### Step 4: Add ADK to PATH (Temporary)
```bash
export PATH=$PATH:$HOME/.local/bin
```

### Step 5: Create First Agent
```bash
adk create firstAgent
```

```text
Choose a model for the root agent:
1. gemini-2.5-flash
Choose model (1, 2): 1

1. Google AI
2. Vertex AI
Choose a backend (1, 2): 1

Enter Google API key: RANDOM_API_KEY_HERE
```

### Step 6: Update Environment Variables
```bash
ls
cd firstAgent
vi .env
```

```text
i      → insert mode
Esc    → command mode
x      → delete character
dd     → delete line
:w     → save
:q     → quit
:wq    → save and quit
:q!    → quit without saving
```

### Step 7: Run the Agent
```bash
cd ..
adk web
adk run firstAgent
```

---

## 💻 VS Code (Windows) – Google AI Backend

### Step 1: Create Virtual Environment
```powershell
python -m venv adk
.\adk\Scripts\activate
```

### Step 2: Install Google ADK
```powershell
pip install --upgrade  google-cloud-aiplatform[agent_engines,adk]>=1.112
```

### Step 3: Create Agent Folder
```powershell
mkdir testAgent
cd testAgent
```

### Step 4: Create Agent
```powershell
adk create firstAgent
```

```text
Choose model (1): gemini-2.5-flash
Choose backend (1): Google AI
Enter Google API key: YOUR_API_KEY
```

### Step 5: Run the Agent
```powershell
adk web
adk run firstAgent
```

---

## 🔁 VS Code – Vertex AI Backend

### Step 1: Create Vertex AI Agent
```powershell
adk create secondAgent
```

```text
Choose model (1): gemini-2.5-flash
Choose backend (2): Vertex AI
Enter Google Cloud project ID: your-project-id
Enter region [us-central1]: us-central1
```

### Step 2: Authenticate Google Cloud
```powershell
pip install gcloud
gcloud auth application-default login
```

### Step 3: Run Vertex AI Agent
```powershell
cd testAgent
adk web
adk run secondAgent
```
## 🚀 Deploy ADK Agent to Agent Engine

### Supported Lab
- Deploy ADK agents to Agent Engine  
  https://www.skills.google/catalog_lab/32019

### Qwikstart Guide
- Agent Engine Quickstart (ADK)  
  https://docs.cloud.google.com/agent-builder/agent-engine/quickstart-adk

---

### Step 1: Open Agent Engine
- Go to **Agent Engine** in Google Cloud Console

---

### Step 2: Create Cloud Storage Bucket
```text
Bucket name: adk_agent_deploy002xxxxx
```

---

### Step 3: Update `.env` File for Deployment
```env
#GOOGLE_GENAI_USE_VERTEXAI=0
#GOOGLE_API_KEY=AIzaSyBxxxxxxxxxxxxxxxx
GOOGLE_CLOUD_PROJECT=project-xxxxxxxxxxxxxxxxx
GOOGLE_CLOUD_REGION=us-central1
```

---

### Step 4: Check Deploy Command Help
```bash
adk deploy --help
```

---

### Step 5: Deploy Agent to Agent Engine
```bash
adk deploy agent_engine firstAgent   --display_name="currency_agent_v2"   --project="project-ee7cb7bb-2d31-45e1-83d"   --region="us-central1"
```

---

### Step 6: Call Deployed Agent
- Run a Python script to invoke the deployed Agent Engine endpoint

---
