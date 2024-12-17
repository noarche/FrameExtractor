import os
import re
import subprocess
from pathlib import Path
from ffmpeg_path import *

main_logo = '''
    [91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m     [91m_[0m[93m_[0m                  [92m_[0m[96m_[0m     [94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m                              
   [94m/[0m [95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m/[0m  [94m_[0m[95m_[0m[91m/[0m [93m/[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m [91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m/[0m [93m/[0m[92m_[0m   [96m/[0m [94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m/[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m [95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m [94m_[0m[95m_[0m[91m_[0m  [93m_[0m[92m_[0m[96m_[0m  [94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m
  [96m/[0m [94m_[0m[95m_[0m[91m/[0m [93m|[0m [92m|[0m[96m/[0m[94m_[0m[95m/[0m [91m_[0m[93m_[0m[92m/[0m [96m_[0m[94m_[0m[95m_[0m[91m/[0m [93m_[0m[92m_[0m [96m`[0m[94m/[0m [95m_[0m[91m_[0m[93m_[0m[92m/[0m [96m_[0m[94m_[0m[95m/[0m  [91m/[0m [93m/[0m[92m_[0m  [96m/[0m [94m_[0m[95m_[0m[91m_[0m[93m/[0m [92m_[0m[96m_[0m [94m`[0m[95m/[0m [91m_[0m[93m_[0m [92m`[0m[96m_[0m[94m_[0m [95m\[0m[91m/[0m [93m_[0m [92m\[0m[96m/[0m [94m_[0m[95m_[0m[91m_[0m[93m/[0m
 [92m/[0m [96m/[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m>[0m  [96m<[0m[94m/[0m [95m/[0m[91m_[0m[93m/[0m [92m/[0m  [96m/[0m [94m/[0m[95m_[0m[91m/[0m [93m/[0m [92m/[0m[96m_[0m[94m_[0m[95m/[0m [91m/[0m[93m_[0m   [92m/[0m [96m_[0m[94m_[0m[95m/[0m [91m/[0m [93m/[0m  [92m/[0m [96m/[0m[94m_[0m[95m/[0m [91m/[0m [93m/[0m [92m/[0m [96m/[0m [94m/[0m [95m/[0m  [91m_[0m[93m_[0m[92m([0m[96m_[0m[94m_[0m  [95m)[0m 
[91m/[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m/[0m[93m_[0m[92m/[0m[96m|[0m[94m_[0m[95m|[0m[91m\[0m[93m_[0m[92m_[0m[96m/[0m[94m_[0m[95m/[0m   [91m\[0m[93m_[0m[92m_[0m[96m,[0m[94m_[0m[95m/[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m/[0m[95m\[0m[91m_[0m[93m_[0m[92m/[0m  [96m/[0m[94m_[0m[95m/[0m   [91m/[0m[93m_[0m[92m/[0m   [96m\[0m[94m_[0m[95m_[0m[91m,[0m[93m_[0m[92m/[0m[96m_[0m[94m/[0m [95m/[0m[91m_[0m[93m/[0m [92m/[0m[96m_[0m[94m/[0m[95m\[0m[91m_[0m[93m_[0m[92m_[0m[96m/[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m/[0m  

'''
print(main_logo)

exitnote = '''
   [91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m                [91m_[0m[93m_[0m   [92m_[0m[96m_[0m[94m_[0m[95m_[0m           
  [91m/[0m [93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m[91m_[0m[93m_[0m[92m_[0m  [96m_[0m[94m_[0m[95m_[0m[91m_[0m  [93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m [91m/[0m  [93m/[0m [92m_[0m[96m_[0m [94m)[0m[95m_[0m[91m_[0m  [93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m 
 [91m/[0m [93m/[0m [92m_[0m[96m_[0m[94m/[0m [95m_[0m[91m_[0m [93m\[0m[92m/[0m [96m_[0m[94m_[0m [95m\[0m[91m/[0m [93m_[0m[92m_[0m  [96m/[0m  [94m/[0m [95m_[0m[91m_[0m  [93m/[0m [92m/[0m [96m/[0m [94m/[0m [95m_[0m [91m\[0m
[93m/[0m [92m/[0m[96m_[0m[94m/[0m [95m/[0m [91m/[0m[93m_[0m[92m/[0m [96m/[0m [94m/[0m[95m_[0m[91m/[0m [93m/[0m [92m/[0m[96m_[0m[94m/[0m [95m/[0m  [91m/[0m [93m/[0m[92m_[0m[96m/[0m [94m/[0m [95m/[0m[91m_[0m[93m/[0m [92m/[0m  [96m_[0m[94m_[0m[95m/[0m
[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m[91m\[0m[93m_[0m[92m_[0m[96m,[0m[94m_[0m[95m/[0m  [91m/[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m/[0m[93m\[0m[92m_[0m[96m_[0m[94m,[0m [95m/[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m/[0m 
                                [95m/[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m/[0m       

'''

VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')  # Supported video file types

def run_ffmpeg_command(command):
    """Runs a command in the shell and returns the output."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out, err

def get_video_duration(video_path):
    """Gets the duration of the video using ffmpeg."""
    command = f'ffmpeg -i "{video_path}"'
    out, err = run_ffmpeg_command(command)
    
    duration_pattern = re.compile(r"Duration:\s(\d+):(\d+):(\d+\.\d+)")
    match = duration_pattern.search(err.decode())
    
    if match:
        h, m, s = map(float, match.groups())
        return h * 3600 + m * 60 + s
    else:
        return None

def create_output_directory(video_name, num_frames):
    """Creates a new output directory with the format {video_name}_{num_frames}_Extracted_Frames."""
    sanitized_video_name = sanitize_path(video_name)
    dir_name = f"{sanitized_video_name}_{num_frames}_Extracted_Frames"
    base_path = Path(dir_name)
    
    # Create the directory
    if not base_path.exists():
        base_path.mkdir(parents=True, exist_ok=True)
    return base_path

def sanitize_path(path):
    """Sanitizes file path to remove special characters."""
    return re.sub(r'[^\w\s-]', '', str(path))

def extract_frames(video_path, num_frames):
    """Extracts frames from the video file."""
    duration = get_video_duration(video_path)
    if duration is None:
        print(f"\033[91mError obtaining video duration for {video_path}. Please ensure the video file is accessible.\033[0m:")
        return

    start_time = 60
    end_time = duration - 60
    total_time = end_time - start_time

    if total_time <= 0:
        print("\033[91mThe video is too short to extract frames with the given parameters. Video must be at least 3-4 min long.\033[0m:")
        return

    fps = num_frames / total_time

    # Get the base name of the video file
    video_name = Path(video_path).stem

    # Create the new output directory
    output_dir = create_output_directory(video_name, num_frames)

    # Sanitize the output directory path
    sanitized_output_dir = sanitize_path(output_dir)

    # Update the frame file naming to use {original_file_name}_{extracted_frame_number}.jpg
    command = (
        f'ffmpeg -i "{video_path}" -vf "fps={fps}" -ss {start_time} -t {total_time} '
        f'-q:v 2 "{sanitized_output_dir}/{video_name}_%04d.jpg"'
    )

    out, err = run_ffmpeg_command(command)
    if err:
        print(f"\033[91mError extracting frames from {video_path}\033[0m:: {err.decode().strip()}")
        return

    print(f"\033[32mFrames successfully saved in\033[0m: {sanitized_output_dir}")

def process_directory(directory_path, num_frames):
    """Processes all video files in the directory."""
    video_files = [f for f in Path(directory_path).rglob("*") if f.suffix.lower() in VIDEO_EXTENSIONS]

    if not video_files:
        print("\033[91mNo video files found in the specified directory.\033[0m:")
        return

    print(f"\033[94mFound {len(video_files)} video(s) in the directory. Processing each...\033[0m")

    for video_file in video_files:
        print(f"\n\033[93mProcessing video: {video_file}\033[0m")
        extract_frames(video_file, num_frames)

def main():
    while True:
        video_path = input("\033[95mEnter the path to the video file or directory\033[0m: ").strip()
        
        # Remove whitespace input
        if not video_path or video_path.isspace():
            print("\033[91mInput cannot be empty. Please try again.\033[0m")
            continue

        video_path = Path(video_path)

        if video_path.is_dir():
            try:
                num_frames = int(input("\033[95mEnter the number of frames to extract for each video\033[0m: "))
                process_directory(video_path, num_frames)
            except ValueError:
                print("\033[91mInvalid input. Please enter a valid number.\033[0m:")
                continue
        elif video_path.is_file() and video_path.suffix.lower() in VIDEO_EXTENSIONS:
            try:
                num_frames = int(input("\033[95mEnter the number of frames to extract\033[0m: "))
                extract_frames(video_path, num_frames)
            except ValueError:
                print("\033[91mInvalid input. Please enter a valid number.\033[0m:")
                continue
        else:
            print("\033[91mInvalid file or directory path. Please try again.\033[0m")
            continue

        choice = input("\033[92mDo you want to process another file or directory? (yes/no)\033[0m: ").strip().lower()
        if choice not in ["yes", "y"]:
            print(exitnote)
            break

if __name__ == "__main__":
    main()
