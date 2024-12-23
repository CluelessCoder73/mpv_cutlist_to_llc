import json

# User Guide for mpv_cutlist_to_llc_v1.2.0.py

"""
mpv_cutlist_to_llc_v1.2.0.py

This script converts a cutlist generated from MPV (in JSON format) into a LosslessCut project file (.llc).
This script was tested and works with:
- Python 3.12.5    
- mpv-x86_64-20240825-git-cb4fdb5
- LosslessCut 3.62.0

Note:
  The "end_buffer_time" feature will not cause any problems if the 
  frames are added at the very end of your input video (if your last 
  segment's end point is at the very last frame of the input video). 
  LosslessCut will display that there are extra frames, but when that 
  last segment is saved, it's end point will be exactly the same as 
  if there were no extra frames added to that end point at all! 
  Likewise, "start_buffer_time" is completely safe also!

How to Use:
1. Specify the paths for the input cutlist file (generated from MPV) and the output .llc project file.
2. Set the name of the media file that you are editing (e.g., "test.mp4").
3. Adjust the buffer times as needed:
   - `start_buffer_time`: The amount of time (in seconds) to subtract from the start of each segment (adds MORE frames!).
   - `end_buffer_time`: The amount of time (in seconds) to add to the end of each segment.
   - Both `start_buffer_time` and `end_buffer_time` accept float values (e.g., 0.5 for half a second).
4. Set `enable_segment_numbering` to True if you want to add automatic segment numbering (e.g., "segment 1", "segment 2").
5. Run the script. The output will be a .llc project file that can be opened in LosslessCut.

The script automatically ensures that the start time of each segment is not negative by setting the start time to 0 if the calculated value would be negative.
"""

# Specify the paths to your input cutlist file and output .llc project file
input_filename = r"C:\New folder\cutlist.txt"
output_filename = r"C:\New folder\project.llc"
media_filename = "test.mp4"  # Specify the media file name

# Buffer times for start and end in seconds
start_buffer_time = 0  # Number of seconds before each segment (float values allowed)
end_buffer_time = 0    # Number of seconds after each segment (float values allowed)

# Option to enable or disable automatic segment numbering
enable_segment_numbering = True  # Set to True to add "segment 1", "segment 2", etc.

def read_timestamps(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        cleaned_lines = [line.rstrip(',\n') for line in lines]
        content = "[" + ",".join(cleaned_lines) + "]"
        cut_segments = json.loads(content)
    return cut_segments

def generate_llc_project(cut_segments, media_filename, output_filename, start_buffer_time, end_buffer_time, enable_segment_numbering):
    project_data = {
        "version": 1,
        "mediaFileName": media_filename,
        "cutSegments": []
    }
    
    for i, segment in enumerate(cut_segments):
        # Apply buffer times to each segment
        start_time = max(segment["start"] - start_buffer_time, 0)  # Ensure start is not negative
        end_time = segment["end"] + end_buffer_time
        
        # Determine segment name based on numbering option
        if enable_segment_numbering:
            segment_name = f"segment {i + 1}"
        else:
            segment_name = ""

        # Add segment with the start, end, and name to the project data
        project_data["cutSegments"].append({
            "start": start_time,
            "end": end_time,
            "name": segment_name,
        })

    # Write the project data to the output .llc file
    with open(output_filename, "w") as file:
        json.dump(project_data, file, indent=4)

# Read the cut segments from the cutlist.txt file
cut_segments = read_timestamps(input_filename)

# Generate the LosslessCut project file with the specified settings
generate_llc_project(cut_segments, media_filename, output_filename, start_buffer_time, end_buffer_time, enable_segment_numbering)
