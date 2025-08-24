import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Set initial default path
selected_path = os.path.join(os.path.expanduser("~"), "Downloads")

def clean_url(url):
    """Clean the YouTube URL by removing extra parameters."""
    return url.strip().split('&')[0]

def change_folder():
    """Allow user to select a new download folder."""
    global selected_path
    folder = filedialog.askdirectory()
    if folder:
        selected_path = folder
        folder_label.config(text=f"Download Folder:\n{selected_path}")

def download():
    raw_url = url_entry.get()
    url = clean_url(raw_url)
    res = resolution_var.get()

    is_audio = res.startswith("audio")

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    if "youtube.com" not in url and "youtu.be" not in url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    # Ensure folder exists
    os.makedirs(selected_path, exist_ok=True)

    try:
        messagebox.showinfo("Downloading", "Download started. Please wait...")

        if is_audio:
            audio_format = res.split("-")[-1].strip()
            cmd = [
                'yt-dlp',
                '-f', 'bestaudio',
                '--extract-audio',
                '--audio-format', audio_format,
                '-o', os.path.join(selected_path, '%(title)s.%(ext)s'),
                url
            ]
        else:
            height = res[:-1]  # Remove 'p'
            cmd = [
                'yt-dlp',
                '-f', f'bestvideo[height={height}]+bestaudio/best',
                '-o', os.path.join(selected_path, '%(title)s.%(ext)s'),
                url
            ]

        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", f"Download completed!\nSaved to: {selected_path}")

    except subprocess.CalledProcessError:
        messagebox.showerror("Download Failed", "An error occurred during the download process.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader (yt-dlp)")
root.geometry("460x300")
root.resizable(False, False)

# URL Input
tk.Label(root, text="Enter YouTube URL:").pack(pady=(15, 0))
url_entry = tk.Entry(root, width=55)
url_entry.pack(pady=5)

# Resolution Dropdown
tk.Label(root, text="Select Resolution / Audio Format:").pack(pady=(10, 0))
resolution_var = tk.StringVar(value="720p")
options = [
    "2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p",
    "audio - mp3", "audio - m4a", "audio - aac", "audio - opus"
]
tk.OptionMenu(root, resolution_var, *options).pack(pady=5)

# Folder Label
folder_label = tk.Label(root, text=f"Download Folder:\n{selected_path}", wraplength=400, justify="center")
folder_label.pack(pady=(5, 0))

# Change Folder Button
tk.Button(root, text="Change Folder", command=change_folder).pack(pady=(5, 0))

# Download Button
tk.Button(root, text="Download", command=download).pack(pady=15)

root.mainloop()
