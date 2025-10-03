
# CareerBot - AI Career Counsellor 🤖👩‍💼
Live app- https://career-chatbot-by-stuti.streamlit.app/ 

## 📌 Project Description

**CareerBot** is a web-based, interactive career counselling chatbot built using **Streamlit** and powered by the **Google Gemini Large Language Model (LLM)**. Its primary purpose is to provide personalized, contextual, and instant guidance on career paths, educational choices, skill development, and job search strategies.

---

## ✨ Features

- **Intelligent Career Advice:** Provides responses based on the powerful `gemini-2.5-flash` model, specifically instructed to act as a career counsellor.  
- **User Authentication:** Secure **Login** and **Sign Up** functionality with persistent accounts.  
- **Secure Password Storage:** User passwords are hashed using **SHA256** before being saved in the database.  
- **Persistent Chat History:** Conversations are saved to an **SQLite database** (`career_chatbot.db`) and retrieved upon login.  
- **Contextual Conversation:** The chatbot sends the last six messages of history to the AI for relevant dialogue.  
- **Chat History Page:** A dedicated page (`pages/chat_history.py`) allows logged-in users to view, download (as CSV), and clear their entire chat history.  

---

## 💡 Usefulness (What it Does)

| Area | Benefit |
| :--- | :--- |
| **Accessibility** | 24/7, on-demand career counseling, overcoming time and geographical constraints. |
| **Personalization** | Remembers past conversations to provide tailored guidance. |
| **Data Security** | Uses `hashlib` for password hashing, protecting credentials. |
| **Scalability** | Web application can serve multiple users simultaneously. |
| **Data Export** | Chat history can be downloaded for review or analysis. |

---

## ⚙️ How It Works (Technical Functioning)

The application combines a **Streamlit front-end**, **SQLite database**, and the **Gemini API** for intelligence.

### 1. Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend/UI** | `streamlit` | Creates the web interface, login forms, and chat popup. |
| **AI/ML Core** | `google.generativeai` (Gemini 2.5 Flash) | Generates career advice. |
| **Database** | `sqlite3` | Stores user credentials (hashed) and chat history. |
| **Dependencies** | `pandas`, `plotly` | For data manipulation and visualization. |

### 2. Key Code Modules

| File | Description | Core Functionality |
| :--- | :--- | :--- |
| **`app.py`** | **Main Application File** | Handles session state, login/signup, CSS styling, and chat logic. |
| **`DatabaseManager` Class (in `app.py`)** | **Data Persistence** | Manages SQLite DB with `create_tables()`, `hash_password()`, `authenticate_user()`, `save_chat()`, `get_chat_history()`. |
| **`CareerChatbot` Class (in `app.py`)** | **AI Logic** | Connects to Gemini model via `get_response()`. |
| **`pages/chat_history.py`** | **History Viewer** | Fetches conversation history, displays, downloads, and clears chats. |
| **`.streamlit/secrets.toml`** | **Security** | Stores Gemini API Key securely. |

---

## 🚀 Setup and Installation

### Prerequisites
- Python 3.9+

### 1. Environment Setup

```bash
# Clone the repository (replace with your repo URL)
git clone <repository_url>
cd CareerBot

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

**Required Packages:**
`streamlit`, `google-generativeai`, `pandas`, `plotly`, `opencv-python`, `numpy`, `Pillow`, `requests`

### 2. API Key Configuration

1. Create a folder named **`.streamlit`** in the project root.
2. Inside `.streamlit`, create a file named **`secrets.toml`**.
3. Add your API key:

```toml
[gemini]
api_key="YOUR_API_KEY_HERE"
```

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser. Sign up to create an account and start chatting with **CareerBot**.

---

## 📂 Repository Structure

```
CareerBot/
│── app.py
│── pages/
│   └── chat_history.py
│── career_chatbot.db
│── requirements.txt
│── .streamlit/
│   └── secrets.toml
│── README.md
```

---

## 🛡️ Security Notes

* Passwords are **never stored in plain text**; they are hashed using **SHA256**.
* API keys are **not hardcoded**; they are securely managed in `.streamlit/secrets.toml`.

---

## 📜 License

This project is licensed under the MIT License.
Feel free to fork and modify for personal or educational use.

---

## 🤝 Contribution

Pull requests are welcome. For major changes, open an issue first to discuss your proposal.



