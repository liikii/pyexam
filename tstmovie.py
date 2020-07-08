"""
"""
from moviepy.editor import ImageClip, afx
from moviepy.editor import concatenate_videoclips, CompositeVideoClip
from moviepy.video.compositing.transitions import slide_in
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.fx.audio_loop import audio_loop
from random import choice


drc = ['top', 'bottom', 'left', 'right', 'top', 'bottom', 'left', 'right', 'top', 'bottom', 'left', 'right']

img0 = ImageClip('static/video_cover_1.jpg')
img0_n = img0.set_duration(4)

clips = [ImageClip('static/video_cover_%s.jpg' % i).set_duration(4) for i in range(2, 8)]


slided_clips = [CompositeVideoClip([clip.fx(slide_in, duration=1, side=choice(drc))]) for clip in clips]
slided_clips.insert(0, img0_n)
final_clip = concatenate_videoclips(slided_clips, method="compose", padding=-1)
music = AudioFileClip("static//aud1593779359532480.m4a")
audio = audio_loop(music, duration=final_clip.duration)
final_clip = final_clip.set_audio(audio)
final_clip.write_videofile("my_concatenation.mp4", fps=26, audio_bitrate="1000k", bitrate="4000k", codec='libx264', audio_codec='aac')
