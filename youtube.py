import yt_dlp
import tkinter as tk
from tkinter import filedialog



def download_video(url, save_path="."):

    options = {
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save with video title as filename
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,  # Download only one video, not a playlist
        "quiet": False,  # Show progress
    }


    # Show available formats
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)  # Get available formats without downloading
        formats = info.get("formats", [])
        print(formats)
        print("\nAvailable Formats:")

        for fmt in formats:

            fmt_id = fmt.get("format_id")
            fmt_note = fmt.get("format_note")
            resolution = fmt.get("resolution", "Audio")  # If no resolution, it's audio
            ext = fmt.get("ext")
            if fmt_note is not None:
                print(f"[{fmt_id}] {resolution} - {fmt_note} ({ext})")


    # Ask the user to choose a format
    format_choice = input("\nEnter format ID (or press Enter for best quality): ").strip()

    if format_choice:
        options["format"] = format_choice  # Download the chosen format
    else:
        options["format"] = "bestvideo+bestaudio/best"  # Default to best quality

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


def open_file_dialog():
    folder_path = filedialog.askdirectory()

    if folder_path:
        print(f"Selected folder: {folder_path}")
    return folder_path


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter YouTube video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Download....")
        download_video(video_url, save_path=save_dir)
    else:
        print("Invalid save location.")
