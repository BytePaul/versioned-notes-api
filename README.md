# 📝 Versioned Notes App

A full-stack note-taking application with automatic version control. Built with **FastAPI** (Python) for the backend and **Streamlit** for the frontend, this app allows users to create, view, and search notes — each update creating a new version.

---

## 🔧 Tech Stack

- **Backend**: FastAPI + SQLite  
- **Frontend**: Streamlit (React under the hood)  
- **Search Autocomplete**: Custom Trie-based prefix matching  
- **Data Persistence**: SQLite (auto-generated on startup)  

---

## ✨ Features

- 🔐 Create notes with title, content, and tags  
- 🕓 Each update creates a new version automatically  
- 🔍 Smart title-based search using Trie data structure  
- 🗂️ View note content and all versions  
- 🆕 Create notes via a separate tab  
- 🔗 View full notes in a new browser tab  
- 💾 Simple local database (SQLite)

---

## 📁 Project Structure

```
versioned-notes-api/
├── main.py                 # FastAPI app entry
├── crud.py                 # DB access logic
├── models.py               # Pydantic schemas
├── database.py             # SQLite setup
├── routers/
│   └── notes.py            # API routes
├── trie.py                 # TitleTrie class
├── streamlit_frontend.py   # Main UI (search/view)
├── new_note_form.py        # Create new note page
├── view_note.py            # Full-screen note viewer
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/versioned-notes-api.git
cd versioned-notes-api
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> This includes `fastapi`, `uvicorn`, `pydantic`, `streamlit`, and `requests`.

---

### 3️⃣ Start the FastAPI Backend

```bash
uvicorn main:app --reload
```

Runs on: [http://localhost:8000](http://localhost:8000)

---

### 4️⃣ Start the Streamlit Apps

Open **3 terminals** and run:

#### 🖥️ Viewer UI (search + versions):

```bash
streamlit run streamlit_frontend.py
```

#### 🆕 New Note Form:

```bash
streamlit run new_note_form.py --server.port 8502
```

#### 🔗 Note Viewer:

```bash
streamlit run view_note.py --server.port 8503
```

Then visit:

- [localhost:8501](http://localhost:8501) → Search/view notes  
- [localhost:8502](http://localhost:8502) → Create new notes  
- [localhost:8503](http://localhost:8503) → View notes in full window

---

## 🧠 Smart Search (Trie)

A custom `TitleTrie` is used to support **fast title-based prefix matching** and metadata retrieval. It auto-loads from the DB on startup.

```http
GET /search-title?q=proj
→ returns matches: [{ title, version, timestamp }]
```

---

## ✅ Future Enhancements

- ✏️ Editable notes (update latest version)  
- 🔍 Diff between versions  
- 🗃️ Export notes as `.txt` or `.pdf`  
- 🔐 Add user authentication  
- ☁️ Deploy via Render, Railway or HuggingFace Spaces  

---

## 📜 License

MIT License © 2025 Paul Gaikwad

---

> Built to never lose track of your thoughts — one version at a time.
