"""
"""
from moviepy.editor import ImageClip, afx, TextClip
from moviepy.editor import concatenate_videoclips, CompositeVideoClip
from moviepy.video.compositing.transitions import slide_in
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.fx.audio_loop import audio_loop
from random import choice


drc = ['top', 'bottom', 'left', 'right', 'top', 'bottom', 'left', 'right', 'top', 'bottom', 'left', 'right']

img0 = ImageClip('static/video_cover_1.jpg')
img0_n = img0.set_duration(4)



# txt = TextClip("比邻", font='Amiri-regular',
# 	               color='white',fontsize=24)
#
# txt_col = txt.on_color(size=(ukulele.w + txt.w,txt.h-10),
#                   color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
#
#
# # THE TEXT CLIP IS ANIMATED.
# # I am *NOT* explaining the formula, understands who can/want.
# txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
#                                   max(5*h/6,int(100*t))) )
#
txt_mov = (TextClip("k·b", fontsize=60,
               font="WenQuanYi-Zen-Hei", color="srgb(255,218,49)").margin(top=15, opacity=0)
                .set_position(("center")).set_start(1))

img0_n = CompositeVideoClip([img0_n, txt_mov]).set_duration(4)
print(type(img0_n))

clips = [ImageClip('static/video_cover_%s.jpg' % i).set_duration(4) for i in range(2, 8)]


slided_clips = [CompositeVideoClip([clip.fx(slide_in, duration=1, side=choice(drc))]) for clip in clips]
slided_clips.insert(0, img0_n)
final_clip = concatenate_videoclips(slided_clips, method="compose", padding=-1)
music = AudioFileClip("static/aud1593779359532480.m4a")
audio = audio_loop(music, duration=final_clip.duration)
final_clip = final_clip.set_audio(audio)



final_clip.write_videofile("my_concatenation.mp4", fps=24, audio_bitrate="1000k", bitrate="4000k", codec='libx264', audio_codec='aac')
