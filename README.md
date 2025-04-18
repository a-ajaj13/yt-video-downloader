# YouTube Video Downloader

This program allows users to download YouTube videos or entire playlists with custom quality preferences. It utilizes the powerful `yt-dlp` library for downloading videos and provides flexibility to choose from available video qualities dynamically. It supports downloading videos to a user-specified directory and handles large downloads efficiently using the `aria2c` external downloader.

## Features

- Download single videos or entire playlists.
- Choose from available video qualities (e.g., 144p, 360p, 720p, 1080p, 4K, etc.).
- Download videos in `mp4` format after merging video and audio.
- Supports specifying a custom download directory.
- External downloader (`aria2c`) for faster and segmented downloads.
- Handles errors gracefully and provides user-friendly messages.

## Requirements

- Python 3.6+
- `yt-dlp` (YouTube downloader)
- `ffmpeg` (for merging video and audio into one file)
- `aria2c` (for faster downloads, optional but recommended)

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/your-username/yt-video-downloader.git
    cd yt-video-downloader
    ```

2. Install the necessary Python dependencies.

    You can install dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Install `aria2c` for improved download performance:

    - **Linux**: `sudo apt install aria2`
    - **macOS**: `brew install aria2`
    - **Windows**: Download from [here](https://aria2.github.io/).

## Usage

### 1. Running the Program

To run the video downloader, execute the following command:

```bash
python downloader.py
```
### 2. Follow the prompts

- URL: Enter the YouTube video or playlist URL you want to download.
- Quality: Choose your preferred video quality (e.g., 720p, 1080p, etc.). The available qualities will be fetched dynamically from the video.
- Directory: Choose whether to use the default download directory or specify a custom location.

The video will be downloaded in the specified format (mp4) to the selected directory.

### Example
```bash
Do you want to download a video or playlist? (v for video/p for playlist): v
Enter YouTube URL: https://www.youtube.com/watch?v=example
Available qualities:
1. 2160p
2. 1440p
3. 1080p
4. 720p
5. 480p
6. 360p
7. 240p
8. 144p

Select quality (enter number): 3

Default Downloads directory is (~\\download\\YouTube), Want to specify another? (y/n): n

Starting download...
Download completed!
```
