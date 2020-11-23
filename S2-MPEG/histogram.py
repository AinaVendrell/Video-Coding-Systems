from pathlib import Path
import os


def histogram():
    input_path = Path.cwd() / "Results/1-cut"
    input_file = str(input_path / "BBB_10.mp4")

    output_path = Path.cwd() / "Results/2-histogram"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path / "BBB_histogram.mp4")

    command = f"ffmpeg -i {input_file} -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay -c:a copy {output_file}"
    os.system(command)
    os.system(f"ffplay {output_file}")
