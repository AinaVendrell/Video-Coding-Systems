from pathlib import Path
import os


def resize(size):
    input_path = Path.cwd() / "Results/1-cut"
    input_file = str(input_path / "BBB_10.mp4")

    output_path = Path.cwd() / "Results/3-resize"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path / "BBB_") + size + ".mp4"

    if 'p' in size:
        size = size.split('p')[0]
        print(size)
        command = f"ffmpeg -i {input_file} -vf scale=-2:{size} -c:a copy {output_file}"

    else:
        command = f"ffmpeg -i {input_file} -vf scale={size},setsar=1 -c:a copy {output_file}"

    os.system(command)
    os.system(f"ffplay {output_file}")
