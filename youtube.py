from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path="."):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4", progressive=True)
        print(stream)
        if not stream:
            print("No progressive MP4 streams available.")
            return

        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)

        print("Video Downloaded Successfully!")
    except Exception as e:
        print(f"Error: {e}")


video_url = "https://youtu.be/g_Pog2fAuAE?si=b09NM7gHzTwQcgVz"
download_video(video_url, save_path="./downloads")

