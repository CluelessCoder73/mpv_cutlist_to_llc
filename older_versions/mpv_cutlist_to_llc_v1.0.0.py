import json

# Specify the paths to your input cutlist file and output .llc project file
input_filename = r"C:\New folder\cutlist.txt"
output_filename = r"C:\New folder\project.llc"
media_filename = "test.mp4"  # Specify the media file name

def read_timestamps(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        cleaned_lines = [line.rstrip(',\n') for line in lines]
        content = "[" + ",".join(cleaned_lines) + "]"
        cut_segments = json.loads(content)
    return cut_segments

def generate_llc_project(cut_segments, media_filename, output_filename):
    project_data = {
        "version": 1,
        "mediaFileName": media_filename,
        "cutSegments": []
    }
    
    for segment in cut_segments:
        project_data["cutSegments"].append({
            "start": segment["start"],
            "end": segment["end"],
            "name": "",
        })

    with open(output_filename, "w") as file:
        json.dump(project_data, file, indent=4)

cut_segments = read_timestamps(input_filename)
generate_llc_project(cut_segments, media_filename, output_filename)
