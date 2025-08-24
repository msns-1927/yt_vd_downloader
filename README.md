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

**System Design:**

**Architecture:** User -> GUI -> pytube -> YouTube Server -> File System

<img width="447" height="447" alt="image" src="https://github.com/user-attachments/assets/097e095f-7730-452f-8fe9-f2f124fc52db" />

**UI Design:**

•	URL Input Box

•	Dropdown for resolution/audio

•	Download Button

•	Folder selection

**Database design:**

<img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/d44ecb34-d7f9-4c84-9646-9b5e324b21b5" />

**Implementation:**

**Tools Used:**

tkinter - GUI framework

subprocess - Running system commands (yt-dlp)

os - File paths, folder creation

yt-dlp - Downloading and processing media

ffmpeg - Media conversion (used by yt-dlp)

**Types of Testing:**
•	Unit Testing

•	GUI Usability Testing

•	Error Handling (invalid URLs, connection loss)

**Results:**

The application successfully downloads YouTube videos in desired resolutions. Audio-only mode works reliably. The GUI provides a clean interface for easy use. Compared to existing tools, this solution is lightweight and customizable.

