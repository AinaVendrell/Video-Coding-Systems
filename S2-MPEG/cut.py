from pathlib import Path
import os


def cut(time):
    time = '00:' + time
    input_path = Path.cwd()
    input_file = str(input_path / "BBB.mp4")

    output_path = Path.cwd() / "Results/1-cut"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path / "BBB_10.mp4")

    command = f"ffmpeg -ss {time} -i {input_file} -t 00:00:10 -c copy {output_file}"
    os.system(command)
    os.system(f"ffplay {output_file}")
