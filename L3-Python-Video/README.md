# L3 - Python & Video

<br/>

Executing the `script.py` file the following menu will appear:

```
[?] Choose an exercise:
 > 1) Create example Container
   2) Create custom Container
   3) Check Broadcasting Standards
   4) Create container and check Broadcasting Standards
```
<br/>

**1. Create example Container**

This option will create:
 - `Containers/example/BBB_cut.mp4` video containing the first minute of the  BBB video.
 - `Containers/example/720p_cut.mp4` video containing the first minute of the  BBB video resized at a resolution of 720p.
 - `Containers/example/BBB_mono.mp4` video containing the audio of the first minute of the BBB video as a mono track encoded in mp3.
 - `Containers/example/BBB_bitrate.mp4` video containing the audio of the first minute of the BBB video with a bitrate of 94K.
 - `Containers/example/subtitles.ass` subtitles of the video in ass format.


 Finally, using this files a new container will be created in `Containers/example.mp4` with the command:

 ```
ffmpeg -i {output_resize} -i {output_mono} -i {output_lower_bitrate} -map 0:v -map 1:a -map 2:a -c:a copy -c:v {video_codec} -vf "ass={output_subtitles}" {output_container}
```
<br/>

**2.  Create custom Container**

This option allows you to create a custom container with the given options:
```
[?] Write the name of the container: customContainer

[?] Define the duration of the trimmed video as mm:ss knowing that the maximun is 10:35: 00:30

[?] Define the width and height as (360x240) or the resolution as (720p): 360x240

[?] Choose a video code among the following options:
 > mpeg2video
   h264

[?] Choose an audio code among the following options:
 > aac
   mp3
   ac3

[?] Define the bitrate of the audio: 100
```

<br/>

**3. Check Broadcasting Standards**

This option will ask you to enter the path of a container, after that it will check which broadcasting standards does it fit. Considering:
- DVB:
  - Video: MPEG2, h.264
  - Audio: AAC, Dolby Digital (AC-3), MP3
- ATCS:
  - Video: MPEG2, h.264
  - Audio: AC-3
- ISDB:
  - Video: MPEG2, h.264
  - Audio: AAC
- DTMB:
  - Video: MPEG2, h.264, AVS, AVS+
  - Audio: DRA, AAC, AC-3, MP2, MP3

<br/>

**4. Create container and check Broadcasting Standards**

This option will execute the exercises 2 and 3
