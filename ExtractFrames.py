import os
import re
import subprocess
from pathlib import Path


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

def create_output_directory(base_dir):
    """Creates a new output directory, incrementing the number if it already exists."""
    base_path = Path(base_dir)
    if not base_path.exists():
        base_path.mkdir()
        return base_path

    i = 1
    while True:
        new_dir = base_path.parent / f"{base_path.name}_{i}"
        if not new_dir.exists():
            new_dir.mkdir()
            return new_dir
        i += 1

def sanitize_path(path):
    """Sanitizes file path to remove special characters."""
    return re.sub(r'[^\w\s-]', '', str(path))

def extract_frames(video_path, num_frames):
    """Extracts frames from the video file."""
    
    duration = get_video_duration(video_path)
    if duration is None:
        print("\033[91mError obtaining video duration. Please ensure the video file is accessible.\033[0m:")
        return

    
    start_time = 60
    end_time = duration - 60
    total_time = end_time - start_time

    if total_time <= 0:
        print("\033[91mThe video is too short to extract frames with the given parameters. Video must be minimum 3-4 min long.\033[0m:")
        return

    fps = num_frames / total_time

    
    output_dir = create_output_directory("frames")

    
    sanitized_output_dir = sanitize_path(output_dir)

    
    command = (
        f'ffmpeg -i "{video_path}" -vf "fps={fps}" -ss {start_time} -t {total_time} '
        f'-q:v 2 "{sanitized_output_dir}/frame_%04d.jpg"'
    )

    out, err = run_ffmpeg_command(command)
    if err:
        print(f"\033[91mError extracting frames\033[0m:: {err.decode().strip()}")
        return

    print(f"\033[32mFrames successfully saved in\033[0m: {sanitized_output_dir}")

def main():
    while True:
        
        video_path = input("\033[95mEnter the path to the video file\033[0m: ").strip()

        
        if not Path(video_path).is_file():
            print("\033[91mInvalid file path. Please try again.\033[0m:")
            continue

        
        try:
            num_frames = int(input("\033[95mEnter the number of frames to extract\033[0m:: "))
        except ValueError:
            print("\033[91mInvalid input. Please enter a valid number.\033[0m:")
            continue

        extract_frames(video_path, num_frames)

        
        choice = input("\033[92mDo you want to extract frames from another video? (yes/no)\033[0m: ").strip().lower()
        if choice not in ["yes", "y"]:
            print(exitnote)
            break

if __name__ == "__main__":
    main()
