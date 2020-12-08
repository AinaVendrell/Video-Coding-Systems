from pathlib import Path
import os


def resize(size, input_file):
    current_filename = input_file.split('/').pop()
    file_name = current_filename.split('.')[0]
    file_type = current_filename.split('.')[1]
    print(file_name)
    print(file_type)
    output_path = Path.cwd() / "Results"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path) + "/" + file_name + "_" + size + "." + file_type

    # if is resoultion (720p, 1080p ...)
    if 'p' in size: 
        size = size.split('p')[0]
        command = f"ffmpeg -i {input_file} -vf scale=-2:{size} -c:a copy {output_file}"
    
    # if is size (100x200, 640x200 ...)
    else: 
        command = f"ffmpeg -i {input_file} -vf scale={size},setsar=1 -c:a copy {output_file}"

    os.system(command)
    os.system(f"ffplay {output_file}")
