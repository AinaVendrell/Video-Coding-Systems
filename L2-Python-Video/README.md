# L2 - Python & Video

<br/>

**1. Get data from the BBB.mp4 container**

A menu will allow you to select which information do you want to get of the `BBB_10.mp4` video.

```
[?] Which data so you want to get:
 > duration
   width,height
   avg_frame_rate
   bit_rate
   codec_name,codec_type
```
Once the type of information is selected tha following command will be exexuted:

```
command = f"ffprobe -v error -show_entries stream=index,{data} -of default=noprint_wrappers=1 {input_file}"
```

This will display the index of the stream and the wished information.

<br/>

**2. Script able to rename a given file**

To rename a file you have to provide the path of the file and the new name without the extension. Then the file will be renamed keeping the extension of the old file.


<br/>

**3. Script able to resize a given file**

To resize a file you have to provide the path of the file and the new size that can be expressed as (720p, 1080p ...) or (360x240 ...).

Then this command

```
ffmpeg -i {input_file} -vf scale={size},setsar=1 -c:a copy {output_file}
```

Will generate a new file with the given size that will be stored in the Results folder.

<br/>

**4. Script that transcodes the BBB.mp4 video**

This option will transcode the `BBB_10.mp4` video with the MPEG2 codec for the video and the ACC codec for the audio using the command:

```
ffmpeg -i {input_file} -c:v mpeg2video -c:a aac {output_file}
```

<br/>

**5. Menu to choose exercise**

Menu to select the exercise to execute:

```
[?] Choose an exercise:
 > 1) Get data from BBB video
   2) Rename video
   3) Resize input
   4) Transcode input into an output with another codec
```
