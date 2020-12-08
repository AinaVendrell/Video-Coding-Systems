# https://trac.ffmpeg.org/wiki/FFprobeTips
from pathlib import Path
import os
import json
import subprocess
import inquirer


def getData():
    menuData = [
        inquirer.List('menuData',
                      message='Which data so you want to get',
                      choices=[
                          'duration',
                          'width,height',
                          'avg_frame_rate',
                          'bit_rate',
                          'codec_name,codec_type',
                      ]
                      ),
    ]

    data = inquirer.prompt(menuData)['menuData']
    input_path = Path.cwd()
    input_file = str(input_path / "BBB_10.mp4")
    command = f"ffprobe -v error -show_entries stream=index,{data} -of default=noprint_wrappers=1 {input_file}"
    os.system(command)
