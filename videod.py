# # -*- coding: utf-8 -*-
# # @Author: Dastan_Alam
# # @Date:   22-03-2024 06:29:32 PM       18:29:32
# # @Last Modified by:   Dastan_Alam
# # @Last Modified time: 22-03-2024 11:35:11 PM       23:35:11




from moviepy.editor import VideoFileClip, concatenate_videoclips

def duplicate_video(input_video, duration_minutes):
    # Load the video clip
    video_clip = VideoFileClip(input_video)
    
    # Get the duration of the input video
    total_duration = video_clip.duration
    
    # Calculate the number of times the video needs to be duplicated
    num_duplicates = int(duration_minutes // (total_duration / 60))
    
    # Create a list to store duplicated video clips
    duplicated_clips = [video_clip] * num_duplicates
    
    # Concatenate the duplicated clips
    final_clip = concatenate_videoclips(duplicated_clips)
    
    # Write the final video to a file
    output_file = "duplicated.mp4"
    final_clip.write_videofile(output_file, codec="libx264")
    
    print("Video duplicated successfully!")


# from moviepy.editor import VideoFileClip, concatenate_videoclips
# import multiprocessing

# def duplicate_video(input_video, duration_minutes):
#     # Load the video clip
#     video_clip = VideoFileClip(input_video)
    
#     # Get the duration of the input video
#     total_duration = video_clip.duration
    
#     # Calculate the number of times the video needs to be duplicated
#     num_duplicates = int(duration_minutes // (total_duration / 60))
    
#     # Define a function to duplicate a single clip
#     def duplicate_clip():
#         return [video_clip] * num_duplicates
    
#     # Distribute the workload across multiple processes
#     with multiprocessing.Pool() as pool:
#         duplicated_clips = pool.map(duplicate_clip, range(multiprocessing.cpu_count()))
    
#     # Concatenate the duplicated clips
#     final_clip = concatenate_videoclips(duplicated_clips)
    
#     # Write the final video to a file
#     output_file = "duplicated.mp4"
#     final_clip.write_videofile(output_file, codec="libx264")
    
#     print("Video duplicated successfully!")

# # # Example usage:
# # input_video = "input.mp4"
# # duration_minutes = 10  # Adjust as needed
# # duplicate_video(input_video, duration_minutes)

