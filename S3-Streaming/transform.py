from pathlib import Path
import os


def transform(size):
    file_name = "BBB_" + size + ".mp4"
    input_file = Path.cwd() / "Assets" / file_name

    output_path = Path.cwd() / "Results" / size
    output_path.mkdir(parents=True, exist_ok=True)

    output_file_VP8 = str(output_path / f"BBB_{size}_VP8")
    output_file_VP9 = str(output_path / f"BBB_{size}_VP9")
    output_file_H265 = str(output_path / f"BBB_{size}_H265")
    output_file_AV1 = str(output_path / f"BBB_{size}_AV1")

    # VP8
    command = f"ffmpeg -i {input_file} -c:v libvpx -c:a libvorbis {output_file_VP8}.webm"
    os.system(command)

    # VP9
    command = f"ffmpeg -i {input_file} -c:v libvpx-vp9 {output_file_VP9}.mp4"
    os.system(command)

    # H265
    command = f"ffmpeg -i {input_file} -c:v libx265 {output_file_H265}.mp4"
    os.system(command)

    # AV1
    command = f"ffmpeg -i {input_file} -c copy {output_file_AV1}.avi"
    os.system(command)

    return [output_file_VP8, output_file_VP9, output_file_H265, output_file_AV1]
    
    # The following command to create the AV1 video using the codec libaom-av1 didn't work because it didn't recognize libaom-av1
    # command = f"ffmpeg -i {input_file} -c:v libaom-av1 {output_file_AV1}.mp4"

