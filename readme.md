# 📻 Retro Radio - Backend

A real-time Django-powered backend for the **Retro Radio** project using Django Channels, Redis, and WebSockets. Audio is streamed via Icecast + FFmpeg, simulating a GTA-style retro radio station.

---

## ⚙️ Tech Stack

- Python 3.10+
- Django 5.1
- Django Channels
- Redis (Cloud or Local)
- Daphne (ASGI server)
- FFmpeg + Icecast2 (for audio streaming)

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

## 📡 Audio Streaming Setup (Icecast + FFmpeg)

### 1. 📥 Download Icecast

* Download from: [https://icecast.org/download.php#windows](https://icecast.org/download.php#windows)
* Extract the folder `icecast_win32_2.4.4` and run `icecast.exe`
* Ensure port `8001` is open and streaming is enabled in `icecast.xml`.

### 2. 📥 Download FFmpeg

* Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
* Add the `ffmpeg/bin` folder to your system PATH (for terminal access).

---

### 3. 🔊 Start Streaming Audio via FFmpeg

Place your MP3 file (e.g. `test.mp3`) in the same directory as `ffmpeg.exe`.

Run this command to loop-broadcast the track:

```bash
ffmpeg -re -stream_loop -1 -i test.mp3 -content_type audio/mpeg -f mp3 icecast://source:retroradio@localhost:8001/stream
```

🧠 This continuously sends `test.mp3` to Icecast, which serves it on:
[http://localhost:8001/stream](http://localhost:8001/stream)

---
### 🎮 Start GTA 5 Style Radio (NonStopPopFM)

1. **Download & Place the Required Tools/Resources:**

   * 🔻 [Icecast](https://icecast.org/download.php)
   * 🔻 [FFmpeg](https://ffmpeg.org/)
   * Place [`NonStopPopFMHostedbyCaraGTA5.mp3`](https://mega.nz/file/KFAUBCZL#05ZrQryO3Os5d3i3jQzsgEzI8m8DAMLkztt7bmlfrF4) manually in the correct folder
   * Click [`NonStopPopFMHostedbyCaraGTA5.mp3`](https://mega.nz/file/KFAUBCZL#05ZrQryO3Os5d3i3jQzsgEzI8m8DAMLkztt7bmlfrF4) to Download !

2. Extract and place them in the correct folders:

   ```
   radiostream/
   ├── Icecast/
   ├── ffmpeg-master-latest-win64-gpl/bin/NonStopPopFMHostedbyCaraGTA5.mp3
   └── ffmpeg-master-latest-win64-gpl/
   ```

3. 🎵 Place your audio file as:

   ```
   radiostream/ffmpeg-master-latest-win64-gpl/bin/NonStopPopFMHostedbyCaraGTA5.mp3
   ```

4. ▶️ Run this script to launch Icecast + FFmpeg stream:

   ```bash
   start_radio_GTA5.bat
   ```

5. ✅ The station will stream continuously on:
   [http://localhost:8001/stream](http://localhost:8001/stream)
   Tune into `100.7 MHz` in your app to listen!

---
## ✅ WebSocket Info

* URL format:

  ```
  ws://localhost:8000/ws/<frequency>/?token=<session_id>
  ```

* If frequency is `100.7`, server will automatically stream `http://localhost:8001/stream`.

* The `token` is required (acts as session ID).

---

## 🎧 Test WebSocket & Audio

Open `test.html` in your browser to test WebSocket messages and auto-play stream.

You will hear "NonStopPopFM by Cara" on `100.7 MHz`.

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
## For Production or DEBUG FALSE

collect static with this command 

```
python manage.py collectstatic
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


