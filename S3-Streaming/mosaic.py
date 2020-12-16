from pathlib import Path
import os


def mosaic(input_files, size):
    output_path = Path.cwd() / "Results" / size
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = str(output_path / "mosaic.mkv")

    # | VP8 | H265 |
    # | VP9 | AV1  |

    command = f'ffmpeg -i {input_files[0]}.webm -i {input_files[1]}.mp4 -i {input_files[2]}.mp4 -i {input_files[3]}.avi -filter_complex " \
        [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
        [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
        [2:v] setpts=PTS-STARTPTS, scale=qvga [a2]; \
        [3:v] setpts=PTS-STARTPTS, scale=qvga [a3]; \
        [a0][a1][a2][a3]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[out]" -map "[out]" -c:v libx264 -t 30 -f matroska {output_file}'

    os.system(command)
    os.system(f"ffplay {output_file}")
