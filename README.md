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
pip install google-adk
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

---

## 📌 Git Ignore
```gitignore
.env
```

---
