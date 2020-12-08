from pathlib import Path
import os


def transcode():
    input_path = Path.cwd()
    input_file = str(input_path / "BBB_10.mp4")

    output_path = Path.cwd() / "Results"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path / "BBB_transcode.mp4")

    command = f"ffmpeg -i {input_file} -c:v mpeg2video -c:a aac {output_file}" # video - MPEG2, audio - ACC
    os.system(command)
    os.system(f"ffplay {output_file}")
