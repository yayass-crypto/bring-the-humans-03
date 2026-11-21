#!/bin/bash
# Assemble makefun-ad.mp4 (1080x1920, 30 fps, 30.0 s) from the 5 body scenes
# plus the official make.fun referral end card (press pack, used as-is).
# The user's referral code is typed into the end-card field once the field
# has come to rest (manifest rest_s 1.433 -> overlay from 28.5 s).
set -euo pipefail
cd "$(dirname "$0")"

CODE="vzc3rnvs"
BODY_END=27.0   # 3.5 + 6.0 + 7.0 + 6.0 + 4.5

# End card at 30 fps (source is 60 fps, 3.0 s, 1080x1920).
ffmpeg -v error -y -i assets/endcard-9x16.mp4 \
  -vf fps=30,format=yuv420p -c:v libx264 -preset medium -crf 18 \
  -video_track_timescale 30 endcard30.mp4

scene() { # $1 png, $2 duration
  echo "-loop 1 -framerate 30 -t $2 -i scenes/$1"
}

ffmpeg -v error -y \
  -loop 1 -framerate 30 -t 3.5 -i scenes/s1-hook.png \
  -loop 1 -framerate 30 -t 6.0 -i scenes/s2-what.png \
  -loop 1 -framerate 30 -t 7.0 -i scenes/s3-how.png \
  -loop 1 -framerate 30 -t 6.0 -i scenes/s4-prize.png \
  -loop 1 -framerate 30 -t 4.5 -i scenes/s5-cta.png \
  -i endcard30.mp4 \
  -filter_complex "\
[0:v]zoompan=z='min(1+0.0004*on,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,fade=t=in:st=0:d=0.35,fade=t=out:st=3.15:d=0.35,format=yuv420p[v0]; \
[1:v]zoompan=z='min(1+0.0004*on,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,fade=t=in:st=0:d=0.35,fade=t=out:st=5.65:d=0.35,format=yuv420p[v1]; \
[2:v]zoompan=z='min(1+0.0004*on,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,fade=t=in:st=0:d=0.35,fade=t=out:st=6.65:d=0.35,format=yuv420p[v2]; \
[3:v]zoompan=z='min(1+0.0004*on,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,fade=t=in:st=0:d=0.35,fade=t=out:st=5.65:d=0.35,format=yuv420p[v3]; \
[4:v]zoompan=z='min(1+0.0004*on,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,fade=t=in:st=0:d=0.35,fade=t=out:st=4.15:d=0.35,format=yuv420p[v4]; \
[5:v]fps=30,format=yuv420p[v5]; \
[v0][v1][v2][v3][v4][v5]concat=n=6:v=1:a=0,drawbox=x=208:y=1230:w=9:h=82:color=white:t=fill:enable='gte(t,28.433)',drawtext=fontfile=fonts/JetBrainsMono-Bold.ttf:text='${CODE}':fontsize=62:fontcolor=0x191419:x=210:y=1271-(ascent-descent)/2:enable='gte(t,28.433)'[v]" \
  -map "[v]" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -r 30 -movflags +faststart makefun-ad.mp4

ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,r_frame_rate,codec_name -of default=noprint_wrappers=1 makefun-ad.mp4
