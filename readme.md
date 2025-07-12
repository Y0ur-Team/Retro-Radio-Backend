# 📻 Retro Radio - Backend

A real-time Django-powered backend for the **Retro Radio** project using Django Channels and WebSockets.

---

## ⚙️ Tech Stack

- Python 3.10+
- Django 5.1
- Django Channels
- Redis (Cloud or Local)
- Daphne (ASGI server)

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Y0ur-Team/Retro-Radio-Backend.git
cd retro-radio-backend
````

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
---

### 4. Create a `.env` File from `.env.example`

At the root of the project, create a `.env` file:
and just put hte real values on hte hte .env

---

### 5. Apply Migrations

```bash
python manage.py migrate
```

---

### 6. Run Development Server (WSGI for testing API) 
at port 80 as we will use port 8000 for WS server

```bash
python manage.py runserver 0.0.0.0:80
```

---

### 8. Run ASGI WebSocket Server (Production/Local)
it will use port 80 

Using Daphne (production-ready):

```bash
daphne retro_radio.asgi:application
```

Or Uvicorn (optional):

```bash
uvicorn retro_radio.asgi:application --reload
```

---

## 💡 Notes

* The WebSocket URL format is:

  ```
  ws://localhost:8000/ws/<frequency>/?token=<your_session_id>
  ```

* The frontend must send the `token` as a **query parameter**, not header (due to browser security).

---

## ✅ Sample WebSocket Test

Open `test.html` in your browser to manually test WebSocket functionality.

---

## 🔌 Redis Options

### 🔹 Use Cloud Redis

Configure your `REDIS_URL` in `.env` as:

```
redis://default:<password>@<host>:<port>
```

### 🔹 Or Local Redis

Install Memurai (on Windows) or Redis (on Linux/macOS), then use:

```
REDIS_URL=redis://localhost:6379
```

---

## 📦 Folder Structure (Important Files)

```
retro_radio/
│
├── retro_radio/
│   ├── settings.py
│   ├── asgi.py          ← ASGI application entry
│   └── urls.py
│
├── core/
│   ├── consumers.py     ← WebSocket consumer
│   ├── routing.py       ← WebSocket URL routing
│   └── models.py
│
├── .env                 ← Contains Redis URL & secret key
├── manage.py
└── requirements.txt
─── index.html           ← for testing hte api ofc
```

---


