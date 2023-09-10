from pytube import YouTube

# Replace 'your_video_url' with the URL of the YouTube video you want to download.
video_url = 'https://www.youtube.com/watch?v=6iCFG_-72bM'

# Create a YouTube object.
yt = YouTube(video_url)

# Filter and get the highest resolution mp4 stream.
mp4_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

# Specify the download location.
download_path = 'videos'

# Download the video to the specified location.
mp4_stream.download(output_path=download_path)

print("Video downloaded successfully.")
