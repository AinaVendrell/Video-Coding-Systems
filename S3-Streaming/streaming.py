from pathlib import Path
import os
import subprocess


def streaming():
    input_file = Path.cwd() / "Assets/BBB.mp4"

    command = f"ffmpeg -re -i {input_file} -vcodec mpeg4 -c:a aac -ac 1 -q:v 3 -b:v 64k -f mpegts udp://@224.2.2.2:2222"
    os.system(command)
