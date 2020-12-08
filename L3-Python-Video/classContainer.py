from pathlib import Path
import os
from utils import cut, resize, mono, subtitles, lower_bitrate, checkDuration, checkSize
import subprocess
import numpy as np
import inquirer


class Container:
    # creates a container with a given name, duration, size, bitrate, audio codec and video codec
    def createContainer(self, result):
        time = '00:' + result['duration']
        video_codec = result['video_codec']

        input_path = Path.cwd()
        input_file = str(input_path / "BBB.mp4")
        subtitles_file = str(input_path / "subtitles.srt")

        output_path = Path.cwd() / "Containers" / result['name']
        output_path.mkdir(parents=True, exist_ok=True)
        output_path_container = Path.cwd() / "Containers"
        output_container = str(output_path_container) + \
            "/" + result['name'] + ".mp4"

        output_cut = cut(input_file, output_path, time)
        output_resize = resize(output_cut, output_path, result['size'])
        output_mono = mono(output_cut, output_path, result['audio_codec'])
        output_subtitles = subtitles(subtitles_file, output_path)
        output_lower_bitrate = lower_bitrate(
            output_cut, output_path, result['bitrate'])

        command = f'ffmpeg -i {output_resize} -i {output_mono} -i {output_lower_bitrate} -map 0:v -map 1:a -map 2:a -c:a copy -c:v {video_codec} -vf "ass={output_subtitles}" {output_container}'
        os.system(command)
        os.system(f"ffplay {output_container}")

        return output_container

    # DVB  -- Video: MPEG2, h.264
    # ATCS -- Video: MPEG2, h.264
    # ISDB -- Video: MPEG2, h.264
    # DTMB -- Video: MPEG2, h.264, AVS, AVS+
    def checkVideoBroadcastingStandard(self, array_codecs):
        video_broadcasting_standard = []
        if ('h264' in array_codecs or 'mpeg2video' in array_codecs):
            video_broadcasting_standard.extend(["DVB", "ATCS", "ISDB", "DTMB"])
        elif ('avs' in array_codecs or 'avs+' in array_codecs):
            video_broadcasting_standard.append("DTMB")

        return video_broadcasting_standard

    # DVB  -- Audio: AAC, Dolby Digital (AC-3), MP3
    # ATCS -- Audio: AC-3
    # ISDB -- Audio: AAC
    # DTMB -- Audio: DRA, AAC, AC-3, MP2, MP3
    def checkAudioBroadcastingStandard(self, array_codecs):
        audio_broadcasting_standard = []
        if 'aac' in array_codecs:
            audio_broadcasting_standard.extend(["DVB", "ISDB", "DTMB"])
        if 'mp3' in array_codecs:
            audio_broadcasting_standard.extend(["DVB", "DTMB"])
        if 'ac3' in array_codecs:
            audio_broadcasting_standard.extend(["DVB", "ATCS", "DTMB"])
        if ("dra" in array_codecs or "mp2" in array_codecs):
            audio_broadcasting_standard.append("DTMB")

        return audio_broadcasting_standard

    def checkBroadcastingStandard(self, input_file):
        proc = subprocess.Popen(
            [f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 {input_file}"], stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
        output, err = proc.communicate()
        array_codecs = str(output).split("'")[1].split('\\n')
        array_codecs.pop()
        a = list(np.unique(array_codecs))
        print('\nCodecs:', a)

        broadcasting_standard = list(set(self.checkVideoBroadcastingStandard(array_codecs)).intersection(
            self.checkAudioBroadcastingStandard(array_codecs)))

        if (len(broadcasting_standard) == 0):
            print("ERROR: This container doesn't fit any broadcasting standard")
        else:
            print('This container fits the following broadcasting standards',
                  broadcasting_standard)

    def menuCreateContainer(self):
        container_menu = [
            inquirer.Text('name',
                          message="Write the name of the container",
                          ),
            inquirer.Text('duration',
                          message="Define the duration of the trimmed video as mm:ss knowing that the maximun is 10:35",
                          ),
            inquirer.Text('size',
                          message="Define the width and height as (360x240) or the resolution as (720p)",
                          ),
            inquirer.List('video_codec',
                          message="Choose a video code among the following options",
                          choices=['mpeg2video', 'h264'],
                          ),
            inquirer.List('audio_codec',
                          message="Choose an audio code among the following options",
                          choices=['aac', 'mp3', 'ac3'],
                          ),
            inquirer.Text('bitrate',
                          message="Define the bitrate of the audio",
                          ),
        ]
        result = inquirer.prompt(container_menu)
        if (checkDuration(result['duration']) and checkSize(result['size'])):
            return result
        return None
