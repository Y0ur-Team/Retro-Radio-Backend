@echo off
setlocal

REM === CONFIGURATION ===
set ICECAST_DIR=radiostream\Icecast\bin
set FFMPEG_DIR=radiostream\ffmpeg-master-latest-win64-gpl\bin
set AUDIO_FILE=NonStopPopFMHostedbyCaraGTA5.mp3
set MOUNT_URL=icecast://source:retroradio@localhost:8001/stream

REM === START ICECAST SERVER ===
echo Starting Icecast...
start "" "%ICECAST_DIR%\icecast.exe"

REM === WAIT FOR ICECAST TO BOOT ===
timeout /t 3 >nul

REM === START FFMPEG STREAMING ===
echo Starting FFmpeg audio stream loop...
start "" "%FFMPEG_DIR%\ffmpeg.exe" -re -stream_loop -1 -i "%FFMPEG_DIR%\%AUDIO_FILE%" -content_type audio/mpeg -f mp3 %MOUNT_URL%

echo All services started.
exit /b
