# FFmpeg Codecs for Da Vinci Resolve

> ffmpeg codecs experiment for Da Vinci Resolve 16.2.5

My choice at this point for video: 

* `prores` if there is enough available space
* `vp9` since DaVinci Resolve 17b8
* `mpeg4` with `-qscale:v 1` for maximum quality with compression

For audio:

* `aac` for MP4 container and then create a separate audio file when editting videos
* `pcm_s24le` for MOV container
* Nothing seems compatible with MP4 container *(without crashing)*

If audio doesn't matter `VP9` in mp4 works. Flac should work for audio, but resolve crashes.

## How to run

Run python script and then check output directories

`$ python convert.py`

Bash script to convert inside directory:

```
$ mkdir -p converted && for file in *.mp4; do
  ffmpeg -i $file -c:v mpeg4 -qscale:v 1 -c:a pcm_s24le converted/$file.mov
done
```

Other interesting calls for ffmpeg

`$ ffmpeg -i <input> -c:v prores_ks -profile:v 3 -qscale:v 9 -vendor ap10 -pix_fmt yuv422p10le -c:a pcm_s24le <output.mov>`

`$ ffmpeg -i <input> -c:v libvpx-vp9 -crf 25 -b:v 0 -c:a flac -strict -2 <output.mp4>`

`$ ffmpeg -i <input> -c:v libvpx-vp9 -crf 25 -b:v 0 -c:a aac -b:a 192k <output.mp4>`

`$ ffmpeg -i <input> -c:v libvpx-vp9 -crf 25 -b:v 0 -an <output.mp4>`
