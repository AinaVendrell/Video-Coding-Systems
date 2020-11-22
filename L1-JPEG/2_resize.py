from pathlib import Path
import os

input_path = Path.cwd()
input_file = str(input_path / "lenna.jpg")

output_path = Path.cwd() / "Results/2-resize"
output_path.mkdir(parents=True, exist_ok=True)

output_file = str(output_path / "lenna_32.jpg")
command = f"ffmpeg -i {input_file} -vf scale=32:-2 {output_file}"
os.system(command)

output_file = str(output_path / "lenna_64.jpg")
command = f"ffmpeg -i {input_file} -vf scale=64:-2 {output_file}"
os.system(command)

output_file = str(output_path / "lenna_128.jpg")
command = f"ffmpeg -i {input_file} -vf scale=128:-2 {output_file}"
os.system(command)

output_file = str(output_path / "lenna_256.jpg")
command = f"ffmpeg -i {input_file} -vf scale=256:-2 {output_file}"
os.system(command)
