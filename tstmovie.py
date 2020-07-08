"""
"""
from moviepy.editor import ImageClip
from moviepy.editor import concatenate_videoclips, CompositeVideoClip
from moviepy.video.compositing.transitions import slide_in
from moviepy.audio.io.AudioFileClip import AudioFileClip


img0 = ImageClip('/tmp/video_cover_1.jpg')
img1 = ImageClip('/tmp/video_cover_2.jpg')
img2 = ImageClip('/tmp/video_cover_3.jpg')


audio = (AudioFileClip("/tmp/1593779359532480.mp4")
         .subclip(1, 10)
         .audio_fadein(1)
         .audio_fadeout(1))


img0_n = img0.set_duration(2)
img1_n = img1.set_duration(2)
# lambda t: ('center', 200+t)
img2_n = img2.set_duration(2)
clips = [img1_n, img2_n]
slided_clips = [CompositeVideoClip([clip.fx(slide_in, duration=1, side='left')]) for clip in clips]
slided_clips.insert(0, img0_n)
final_clip = concatenate_videoclips(slided_clips, method="compose", padding=-1).set_audio(audio)

# final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("my_concatenation.mp4", fps=26, audio_bitrate="1000k", bitrate="4000k", codec='libx264',
  audio_codec='aac')
