
---
# 📧 AI Email Triage Agent

An intelligent email analysis and triage service built with **FastAPI**, powered by **Google Gemini AI**, and integrated with **Telex A2A (Agent-to-Agent)** workflows.

This agent receives email data (sender + body), analyzes it using a Gemini model, and classifies it into categories such as **spam**, **inquiry**, **support**, or **invoice** — while also suggesting professional reply drafts.

---

## 🚀 Features

- 🧠 **AI-Powered Email Classification** — Uses Gemini AI to summarize and categorize emails.  
- 📨 **JSON-RPC & A2A Compatible** — Supports direct API calls and Telex A2A integrations.  
- 💬 **Suggested Reply Drafts** — Generates concise, context-aware professional responses.  
- ⚙️ **FastAPI Backend** — Clean, asynchronous architecture ready for production.  
- 🔐 **Secure Key Handling** — Uses `.env` for storing sensitive Gemini API keys.  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python 3.13 |
| **Framework** | FastAPI |
| **AI Model** | Google Gemini 1.5 Flash |
| **Agent Runtime** | Pydantic AI (`pydantic_ai`, `pydantic_ai.models.gemini`) |
| **Integration** | Telex A2A JSON-RPC compatible endpoints |
| **Deployment** | Railway / Render / Docker |
| **Environment Management** | Python-dotenv |

---

## 🧱 Project Structure

```

app/
├── agent/
│   └── agent.py            # Defines the AI logic using Gemini + Pydantic AI
├── routes/
│   └── routes.py           # FastAPI routes for A2A and JSON-RPC endpoints
├── models/
│   └── models.py           # Pydantic models (EmailInput, EmailTriageOutput, A2ARequest, etc.)
├── main.py                 # FastAPI app initialization
└── .env                    # Contains GEMINI_API_KEY

````

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/RashidSWE/hng-emailTriage-AI.git
cd hng-emailTriage-AI
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

Your API will be available at **[http://localhost:8000](http://localhost:8000)**.

---

## 📡 API Endpoints

### **1️⃣ POST /a2a/analyze-email**

A2A-compatible endpoint that other agents or services can call.

#### Request Body

```json
{
  "input": {
    "sender": "ceo@gmail.com",
    "body": "Please confirm the budget for tomorrow's meeting."
  }
}
```

#### Response

```json
{
  "output": {
    "summary": "Sender requests budget confirmation for a meeting.",
    "category": "inquiry",
    "urgency": "medium",
    "suggested_reply_draft": "Sure, I’ll confirm the budget before tomorrow’s meeting."
  },
  "usage": {
    "model": "gemini-1.5-flash",
    "tokens_used": 234
  },
  "status": "success"
}
```

---

### **2️⃣ POST /a2a/jsonrpc**

JSON-RPC 2.0 compatible endpoint for Telex A2A workflows.

#### Request Example

```json
{
  "jsonrpc": "2.0",
  "method": "analyze_email",
  "params": {
    "input": {
      "sender": "hr@company.com",
      "body": "Here’s your payslip for this month."
    }
  },
  "id": 1
}
```

#### Response Example

```json
{
  "jsonrpc": "2.0",
  "result": {
    "output": {
      "summary": "HR sent a monthly payslip.",
      "category": "invoice",
      "urgency": "low",
      "suggested_reply_draft": "Thank you for sharing the payslip."
    },
    "usage": {
      "model": "gemini-1.5-flash",
      "tokens_used": 221
    },
    "status": "success"
  },
  "id": 1
}
```

---

## 🤝 Telex Integration

This agent can be added as a **custom A2A node** inside a Telex workflow.

### Example Node Configuration:

```json
{
  "id": "email_triage_agent_001",
  "name": "Email Triage Agent",
  "type": "a2a/custom-a2a-node",
  "typeVersion": 1,
  "url": "https://hng-emailtriage-ai-production.up.railway.app//a2a/jsonrpc",
  "category": "productivity",
  "description": "An AI-powered email triage agent that classifies and summarizes emails."
}
```

Once deployed, Telex can call your agent with `method: "analyze_email"`.

---

## 🧠 How It Works

1. A user or connected agent sends an email payload to `/a2a/jsonrpc`.
2. The FastAPI app formats the request and sends it to the Gemini AI model.
3. The Gemini model returns a structured output (summary, category, urgency, and draft).
4. The response is returned , ready for display or further workflow automation.

---

## 🧰 Example Use Cases

* Email triage automation for support inboxes
* Smart assistants that prioritize urgent emails
* Internal company bots integrated with Telex workflows
* Teaching AI workflow integration via JSON-RPC

---

## 🛠️ Troubleshooting

| Issue                        | Fix                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------- |
| `Illegal header value` error | Remove newline characters (`\n`) in your API key in `.env`.                   |
| Empty output                 | Check your Gemini model access or API key validity.                           |
| JSON serialization errors    | Make sure `result.output` is converted with `.model_dump()` before returning. |

---

## 🧑‍💻 Author

**Rashid Abdirashid**
💼 Software Engineer
📧 [rashidsamadina@gmail.com](mailto:rashidsamadina@gmail.com)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

## ⭐ Acknowledgments

* [Telex.ai](https://telex.ai) — for providing the A2A integration platform
* [Pydantic AI](https://ai.pydantic.dev) — for structured agent development
* [Google Gemini API](https://ai.google.dev) — for LLM-powered intelligence

```

---
```
