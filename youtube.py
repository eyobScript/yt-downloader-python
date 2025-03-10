import yt_dlp
import tkinter as tk
from tkinter import filedialog


def download_video_or_audio(url, save_path="."):
    """
    Downloads video or audio based on user choice and merges if both are selected.
    """

    # Show available formats
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)  # Get available formats without downloading
        formats = info.get("formats", [])
        video_formats = []
        audio_formats = []
        print(formats)
        # Separate video and audio formats
        for fmt in formats:
            if "video" in fmt["format_note"]:
                video_formats.append(fmt)
            elif "audio" in fmt["format_note"]:
                audio_formats.append(fmt)

        # Print available video formats
        print("\nAvailable Video Formats:")
        for fmt in video_formats:
            fmt_id = fmt.get("format_id")
            resolution = fmt.get("resolution", "No Resolution")
            ext = fmt.get("ext")
            print(f"[{fmt_id}] {resolution} ({ext})")

        # Print available audio formats
        print("\nAvailable Audio Formats:")
        for fmt in audio_formats:
            fmt_id = fmt.get("format_id")
            audio_quality = fmt.get("audio_quality", "Unknown")
            ext = fmt.get("ext")
            print(f"[{fmt_id}] Audio Quality: {audio_quality} ({ext})")

    # Ask the user to choose between video or audio
    media_choice = input("\nDo you want to download 'video' or 'audio'? ").strip().lower()

    # Initialize the options dictionary for yt-dlp
    options = {
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save with video title as filename
        "noplaylist": True,  # Download only one video, not a playlist
        "quiet": False,  # Show progress
    }

    if media_choice == "video":
        format_choice = input("\nEnter video format ID: ").strip()
        options["format"] = format_choice  # Set video format
        options["merge_output_format"] = "mp4"  # Ensure the output is in mp4 format after merging
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    elif media_choice == "audio":
        format_choice = input("\nEnter audio format ID: ").strip()
        options["format"] = format_choice  # Set audio format
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    else:
        print("Invalid choice. Please choose either 'video' or 'audio'.")


def open_file_dialog():
    """
    Opens a file dialog for the user to select a directory.
    """
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Selected folder: {folder_path}")
    return folder_path


if __name__ == "__main__":
    # Initialize Tkinter root
    root = tk.Tk()
    root.withdraw()

    # Get YouTube video URL from the user
    video_url = input("Please enter YouTube video URL: ")

    # Get the folder to save the video
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Download....")
        download_video_or_audio(video_url, save_path=save_dir)
    else:
        print("Invalid save location.")
