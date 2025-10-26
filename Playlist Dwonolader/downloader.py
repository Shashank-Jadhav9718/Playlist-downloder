import streamlit as st
from pytube import Playlist, YouTube
import os
import re

# --- Helper Functions ---

# Function to safely download a video
def download_video(video_object, quality_itag, output_path="downloads"):
    """Downloads a single video with the selected quality (itag)."""
    try:
        # Create the download directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Handle special quality options ('highest_res', 'lowest_res')
        if quality_itag == "highest_res":
            stream = video_object.streams.get_highest_resolution()
        elif quality_itag == "lowest_res":
            stream = video_object.streams.get_lowest_resolution()
        else:
            # Get the stream with the selected specific itag
            stream = video_object.streams.get_by_itag(quality_itag)

        if stream:
            st.info(f"Downloading: **{video_object.title}**...")
            stream.download(output_path=output_path)
            st.success(f"✅ Downloaded: **{video_object.title}**")
        else:
            st.warning(f"⚠️ Could not find a suitable stream for **{video_object.title}** with selected quality.")

    except Exception as e:
        st.error(f"❌ An error occurred while downloading **{video_object.title}**: {e}")


def is_playlist_url(url):
    """Checks if the URL contains a playlist identifier."""
    # Common patterns for YouTube playlist URLs
    return re.search(r'list=|playlist\?', url)


# --- Streamlit App Setup ---

st.set_page_config(
    page_title="YouTube Downloader (Video & Playlist)",
    layout="centered"
)

st.title("▶️ YouTube Downloader")
st.markdown("Enter a **YouTube video URL** or a **playlist URL** and select the quality.")

# Input for the URL
url_input = st.text_input("Enter Video or Playlist URL:")

# Default quality options (ITAGs or special commands)
QUALITY_OPTIONS = {
    "Highest Resolution (Best)": "highest_res",
    "720p MP4 (Combined)": 22,
    "360p MP4 (Combined)": 18,
    "Lowest Resolution (Fastest)": "lowest_res",
}

# Streamlit selectbox for quality selection
quality_selection = st.selectbox(
    "Select Download Quality:",
    options=list(QUALITY_OPTIONS.keys())
)

# Button to start the download
if st.button("Start Download", type="primary") and url_input:
    # Get the selected ITAG or special command string
    selected_itag = QUALITY_OPTIONS[quality_selection]

    if is_playlist_url(url_input):
        # --- Handle Playlist Download ---
        st.subheader("Playlist Download Mode")
        try:
            p = Playlist(url_input)
            st.info(f"Playlist found: **{p.title}** with {len(p.videos)} videos.")

            for video in p.videos:
                # Ensure the video object is fully loaded/refreshed
                video.bypass_age_gate()
                video.check_availability()
                download_video(video, selected_itag)
                
            st.balloons()
            st.success("🎉 **Playlist Download Complete!** All attempted videos have been processed.")

        except Exception as e:
            st.error(f"An error occurred while fetching the playlist: {e}")
            st.error("Please check the playlist URL.")
            
    else:
        # --- Handle Single Video Download ---
        st.subheader("Single Video Download Mode")
        try:
            yt = YouTube(url_input)
            
            # Ensure the video object is fully loaded/refreshed
            yt.bypass_age_gate()
            yt.check_availability()
            
            st.info(f"Video found: **{yt.title}**")
            download_video(yt, selected_itag)
            
            st.success("✅ **Video Download Complete!**")

        except Exception as e:
            st.error(f"An error occurred while fetching the video: {e}")
            st.error("Please check the video URL.")