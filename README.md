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

<img width="552" height="392" alt="Picture1" src="https://github.com/user-attachments/assets/cdf3fdf5-077a-4648-acd6-0a6ed8df1cd8" />

<img width="446" height="261" alt="Picture2" src="https://github.com/user-attachments/assets/08424760-5c37-40a2-9ed4-3ea0d7ab0688" />

<img width="635" height="126" alt="Picture3" src="https://github.com/user-attachments/assets/44e612b5-e8a0-45df-bd10-540f33347b35" />

<img width="434" height="226" alt="Picture4" src="https://github.com/user-attachments/assets/6ac3c6de-9bbc-4b3f-87ea-f3b7a09d5cee" />
