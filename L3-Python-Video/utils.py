import os


def cut(input_file, output_path, time):
    output_file = str(output_path / "BBB_cut.mp4")
    command = f"ffmpeg -ss 00:00:00 -i {input_file} -t {time} -c copy {output_file}"
    os.system(command)
    return output_file


def resize(input_file, output_path, size):
    output_file = str(output_path / "BBB_") + size + ".mp4"
    if 'p' in size:
        size = size.split('p')[0]
        command = f"ffmpeg -i {input_file} -vf scale=-2:{size} -c:a copy {output_file}"
    else:
        command = f"ffmpeg -i {input_file} -vf scale={size},setsar=1 -c:a copy {output_file}"
    os.system(command)
    return output_file


def mono(input_file, output_path, codec):
    name = "BBB_mono." + codec
    output_file = str(output_path / name)
    command = f"ffmpeg -i {input_file} -c:a {codec} -ac 1 {output_file}"
    os.system(command)
    return output_file


def lower_bitrate(input_file, output_path, bitrate):
    output_file = str(output_path / "BBB_bitrate.mp3")
    command = f"ffmpeg -i {input_file} -b:a {bitrate}k {output_file}"
    os.system(command)
    return output_file


def subtitles(subtitles_file, output_path):
    output_subtitles = str(output_path / "subtitles.ass")
    command = f"ffmpeg -i {subtitles_file} {output_subtitles}"
    os.system(command)
    return output_subtitles


def checkDuration(duration):
    a = duration.split(':')
    if int(a[0]) < 11 and int(a[1]) < 61:
        return True
    print('\nDuration: ', duration)
    print('Invalid option, start again and choose a valid duration\n')
    return False


def checkSize(size):
    if 'p' in size or 'x' in size:
        return True
    print('\nSize: ', size)
    print('Invalid option, start again and choose a valid size\n')
    return False
