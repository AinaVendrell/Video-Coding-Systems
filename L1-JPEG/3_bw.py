from pathlib import Path
import os

input_path = Path.cwd()
input_file = str(input_path / "lenna.jpg")

output_path = Path.cwd() / "Results/3-bw"
output_path.mkdir(parents=True, exist_ok=True)

output_file_bw = str(output_path / "lenna_bw.jpg")
command = f"ffmpeg -i {input_file} -vf format=gray {output_file_bw}"
os.system(command)

output_file = str(output_path / "lenna_bw_compressed.jpg")
command = f"ffmpeg -y -i {output_file_bw} -q:v 10 {output_file}"
os.system(command)
