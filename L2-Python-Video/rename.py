from pathlib import Path
import os


def rename(current_file_path, new_name):
    split_path = current_file_path.split('/')
    current_filename = split_path.pop() 
    file_type = current_filename.split('.')[1] # get the type of the file (mp4, mp3, png, jpg ...)
    file_path = "/".join(split_path) # get the path without the file

    new_file_path = file_path + "/" + new_name + "." + file_type
    os.rename(current_file_path, new_file_path)
