import subprocess, os


class FileHandler:
    def download_and_convert_video(self, video_id):
        cmd = f"yt-dlp -f 'bestvideo+bestaudio/best' --merge-output-format mkv --embed-metadata --embed-thumbnail --embed-subs --add-metadata -o '%(title)s.%(ext)s' 'https://www.youtube.com/watch?v={video_id}'" 
        subprocess.run(cmd, shell=True, capture_output=True)
        
    def clean_up(self):
        for file in os.listdir():
            if file.endswith("mkv"):
                os.remove(file)

    def get_file(self):
        for file in os.listdir():
            if file.endswith("mkv"):
                return file