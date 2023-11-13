from video.durevideo import dure
from video.videogif import video_to_gif
inputla="C:\\Users\\IPEPH\\Desktop\\videol4\\vi.mp4"
inputla1=inputla.replace(".mp4","")
if dure(inputla)<=10:
    video_to_gif(f"{inputla}", f"{inputla1}.gif", fps=10)
else:
    print("video a pa dwe dire plis ke 10s tandiske videow la dire", dure(inputla),"s")
