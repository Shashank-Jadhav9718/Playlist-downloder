# ▶️ YouTube Downloader (Video & Playlist)

This is a Python application built with **Streamlit** and **Pytube** that provides a simple web interface for downloading single YouTube videos or entire playlists. It allows the user to select the desired video quality before starting the download.

The application automatically determines whether a URL is for a single video or a playlist and processes the download accordingly.

## ⚠️ Important Note on Privacy

Due to restrictions enforced by YouTube's API and terms of service, this downloader can **only** access and download content that is set to **Public** or **Unlisted**.

* **Public:** Downloadable.
* **Unlisted:** Downloadable (if you have the link).
* **Private:** **Cannot be downloaded.** The application will return an `HTTP Error 403: Forbidden`.

***

## ✨ Features

* **Dual Functionality:** Accepts a single YouTube video URL or a full playlist URL.
* **Quality Selection:** Allows the user to choose from several quality options (e.g., Highest Resolution, 720p, 360p).
* **Interactive UI:** Built using Streamlit for a simple, browser-based user experience.
* **Playlist Processing:** Iterates through every video in a playlist and downloads them sequentially.
* **Automatic Saving:** Downloads are saved to a local folder named `downloads/`.

