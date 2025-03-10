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


def open_file_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Selected folder: {folder_path}")
    return folder_path



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please inter you tube video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Download....")
        download_video(video_url, save_path="./downloads")

