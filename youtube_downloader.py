import os
from yt_dlp import YoutubeDL

def get_video_quality(url: str) -> str:
    """Get user's preferred video quality."""
    # Get the available formats using yt-dlp
    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        
    # Extract the unique available resolutions
    available_qualities = sorted(set(f['height'] for f in formats if 'height' in f), reverse=True)
    
    # Display the available qualities to the user
    print("\nAvailable qualities:")
    for i, quality in enumerate(available_qualities, 1):
        print(f"{i}. {quality}")
    
    while True:
        try:
            choice = int(input("\nSelect quality (enter number): "))
            if 1 <= choice <= len(available_qualities):
                return f"{available_qualities[choice - 1]}"
        except ValueError:
            pass
        print(f"Please enter a number between 1 and {len(available_qualities)}")

def download_video(url: str, quality: str,is_playlist: bool, output_dir: str = None) -> None:
    """Download video with specified quality."""
    try:
        if output_dir is None:
            # Gets the full path to the user’s home directory and ensure the base folder (Downloads/YouTube) exists 
            output_dir = os.path.join(os.path.expanduser("~"), "Downloads", "YouTube")  
            os.makedirs(output_dir, exist_ok=True)

        # Adjust output template based on type
        output_template = (
            os.path.join(output_dir, '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s')
            if is_playlist else
            os.path.join(output_dir, '%(title)s.%(ext)s')
        )

        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            'outtmpl': output_template,
            # 'noplaylist': not is_playlist, no need for this YT-dlp can decide by its automatically from the url provided
            'restrictfilenames': True,
            'external_downloader': 'aria2c',
            'external_downloader_args': [
                '--summary-interval=1',
                '-x', '16',   # Max connections per server
                '-s', '16',   # Split into 16 segments
                '-k', '1M'    # Segment size
            ],
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',  # Convert to mp4 after merging
                }
            ],
            # 'merge_output_format': 'mp4',
            # 'quiet': False,
            # 'no_warnings': True,
            # 'progress': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        raise

def main():
    try:
        # Get video URL
        is_playlist = input("Do you want to download a video or playlist? (v for video/p for playlist): ").strip().lower() == 'p'
        url = input("Enter YouTube URL: ").strip()
        if not ("youtube.com/" in url or "youtu.be/" in url):
            print("Please enter a valid YouTube URL")
            return



        # Get quality preference
        quality = get_video_quality(url)

        # Get output directory preference
        use_current = input("\nDefault Downloads directory is \"~\\download\\YouTube\", Want to specify another? (y/n): ").lower().strip()
        output_dir = None
        if use_current == 'y':
            output_dir = input("Enter download directory path: ").strip()
            if not os.path.exists(output_dir):
                auto_create = input("Directory doesn't exist, want to create it? (y/n)").strip().lower()
                if auto_create:
                    try:
                        os.makedirs(output_dir, exist_ok=True)
                    except Exception as e:
                        print(f"Failed to create directory: {e}")
                        return
                else:
                    return

        # Download video
        print("\nStarting download...")
        download_video(url, quality, is_playlist, output_dir)
        print("\nDownload completed!")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"\nError: {str(e)}")
    finally:
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()