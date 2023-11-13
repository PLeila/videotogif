from moviepy.editor import VideoFileClip
def dure(input_video):
    video_clip = VideoFileClip(input_video)
    duration = video_clip.duration
    video_clip.close()
    return int(duration)