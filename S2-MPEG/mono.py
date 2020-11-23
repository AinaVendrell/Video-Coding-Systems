from pathlib import Path
import os


def mono(codec):
    input_path = Path.cwd() / "Results/1-cut"
    input_file = str(input_path / "BBB_10.mp4")

    output_path = Path.cwd() / "Results/4-mono"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path / "BBB_mono_") + codec + ".mp4"

    command = f"ffmpeg -i {input_file} -acodec {codec} -ac 1 {output_file}"
    os.system(command)

