import moviepy.editor as moviepy

clip = moviepy.VideoFileClip(f"video/video-1.webm")
clip.write_videofile(f"video/video-1.mp4")
