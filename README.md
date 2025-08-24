# yt_vd_downloader
A simple Tkinter-based YouTube downloader built with Python and yt-dlp. Supports multiple resolutions and audio formats with a user-friendly interface.

With the increasing consumption of online video content, users often require offline access to videos. YouTube does not provide an official method for direct downloads. This project offers a practical solution using open-source Python tools.

**Objectives:**

•	Download YouTube videos in selected resolutions

•	Provide audio-only download option

•	Allow folder selection for saving files

**Scope:**

•	User-friendly GUI interface

•	Python-based lightweight tool

•	Downloads individual videos (playlist support can be added)

**Requirements:**

•	Python

•	pytube library

•	tkinter for GUI

•	Internet connection for video access

•	ffmpeg, ffprobe

System Design:
**Architecture:** User -> GUI -> pytube -> YouTube Server -> File System

<img width="447" height="447" alt="image" src="https://github.com/user-attachments/assets/097e095f-7730-452f-8fe9-f2f124fc52db" />
