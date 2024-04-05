# # -*- coding: utf-8 -*-
# # @Author: Dastan_Alam
# # @Date:   22-03-2024 10:32:03 PM       22:32:03
# # @Last Modified by:   Dastan_Alam
# # @Last Modified time: 22-03-2024 11:45:26 PM       23:45:26
# import cv2
# import numpy as np
# from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
# import threading

# def adjust_audio(video_clip, audio_clip):
#     video_duration = video_clip.duration
#     audio_duration = audio_clip.duration
    
#     if audio_duration > video_duration:
#         audio_clip = audio_clip.subclip(0, video_duration)
#     elif audio_duration < video_duration:
#         loops_needed = int(-(-video_duration // audio_duration))  # Convert to integer
#         audio_clip = concatenate_audioclips([audio_clip] * loops_needed)
#         audio_clip = audio_clip.subclip(0, video_duration)
    
#     return audio_clip

# def add_text_to_frame(frame, text, position=(50, 50), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
#     # Convert frame to NumPy array
#     frame = np.array(frame)
#     # Get the dimensions of the frame
#     frame_height, frame_width, _ = frame.shape
#     # Calculate the position for the top-right corner
#     text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
#     text_width, text_height = text_size[0], text_size[1]
#     x = frame_width - text_width - position[0]
#     y = position[1]
#     # Add text to the frame
#     cv2.putText(frame, text, (x, y), font, font_scale, color, thickness)
#     return frame

# def process_frames_with_text(video_clip, text):
#     # Apply text to each frame of the video
#     return [add_text_to_frame(frame, text) for frame in video_clip.iter_frames()]

# def merge_video_audio(video_file, audio_file, output_file, text=None, intro_file=None, outro_file=None):
#     video_clip = VideoFileClip(video_file)
#     audio_clip = AudioFileClip(audio_file)
#     adjusted_audio = adjust_audio(video_clip, audio_clip)
    
#     intro_clip = VideoFileClip(intro_file).subclip(0, 5) if intro_file else None
#     outro_clip = VideoFileClip(outro_file).subclip(0, 5) if outro_file else None
    
#     if text:
#         # Add text to each frame of the video
#         frames_with_text = process_frames_with_text(video_clip, text)
#         # Create a new video clip from frames with text
#         video_clip = video_clip.fl_image(lambda img: add_text_to_frame(img, text))
#         video_clip.write_videofile(output_file, audio=adjusted_audio, codec="libx264")
    
#     # Combine video clips and write the final video
#     clips = [clip for clip in [intro_clip, video_clip.set_audio(adjusted_audio), outro_clip] if clip]
#     final_clip = concatenate_videoclips(clips, method="compose")
#     final_clip.write_videofile(output_file, codec="libx264", threads=4)  
#     # Adjust threads as needed
    
#     print("Video and audio merged successfully!")

# # # Example usage:
# # video_file = "duplicated.mp4"
# # audio_file = "binaural_beat.wav"
# # output_file = "DONE.mp4"
# # text = "FILMSTOCK HD"
# # intro_file = "intro.mp4"
# # outro_file = "outro.mp4"

# # merge_video_audio(video_file, audio_file, output_file, text, intro_file, outro_file)


import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips

def adjust_audio(video_clip, audio_clip):
    video_duration = video_clip.duration
    audio_duration = audio_clip.duration
    
    if audio_duration > video_duration:
        audio_clip = audio_clip.subclip(0, video_duration)
    elif audio_duration < video_duration:
        loops_needed = int(-(-video_duration // audio_duration))  # Convert to integer
        audio_clip = concatenate_audioclips([audio_clip] * loops_needed)
        audio_clip = audio_clip.subclip(0, video_duration)
    
    return audio_clip

def add_text_to_frame(frame, text, position=(50, 50), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
    # Convert frame to NumPy array
    frame = np.array(frame)
    # Get the dimensions of the frame
    frame_height, frame_width, _ = frame.shape
    # Calculate the position for the top-right corner
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_width, text_height = text_size[0], text_size[1]
    x = frame_width - text_width - position[0]
    y = position[1]
    # Add text to the frame
    cv2.putText(frame, text, (x, y), font, font_scale, color, thickness)
    return frame

def process_frames_with_text(video_clip, text):
    # Apply text to each frame of the video
    return [add_text_to_frame(frame, text) for frame in video_clip.iter_frames()]

def merge_video_audio(video_file, audio_file, output_file, text=None, intro_file=None, outro_file=None):
    try:
        video_clip = VideoFileClip(video_file)
        audio_clip = AudioFileClip(audio_file)
        adjusted_audio = adjust_audio(video_clip, audio_clip)
        
        intro_clip = VideoFileClip(intro_file).subclip(0, 5) if intro_file else None
        outro_clip = VideoFileClip(outro_file).subclip(0, 5) if outro_file else None
        
        if text:
            # Add text to each frame of the video
            frames_with_text = process_frames_with_text(video_clip, text)
            # Create a new video clip from frames with text
            video_clip = video_clip.fl_image(lambda img: add_text_to_frame(img, text))
            video_clip.write_videofile(output_file, audio=adjusted_audio, codec="libx264")
        
        # Combine video clips and write the final video
        clips = [clip for clip in [intro_clip, video_clip.set_audio(adjusted_audio), outro_clip] if clip]
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(output_file, codec="libx264", threads=4)  
        # Adjust threads as needed
        
        print("Video and audio merged successfully!")
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Close video and audio clips
        if 'video_clip' in locals():
            video_clip.close()
        if 'audio_clip' in locals():
            audio_clip.close()

# # Example usage:
# video_file = "duplicated.mp4"
# audio_file = "binaural_beat.wav"
# output_file = "DONE.mp4"
# text = "FILMSTOCK HD"
# intro_file = "intro.mp4"
# outro_file = "outro.mp4"

# merge_video_audio(video_file, audio_file, output_file, text, intro_file, outro_file)
