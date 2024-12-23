# mpv_cutlist_to_llc
This script converts a cutlist generated from MPV (in JSON format) into a LosslessCut project file (.llc).
MPV Script: "log_timestamps.lua" - This script logs timestamps to cutlist.txt with each pair of key presses marking a start and and end point.

Step-by-Step Instructions

    Place "log_timestamps.lua" in the appropriate directory for MPV scripts:
            On Linux: ~/.config/mpv/scripts/
            On Windows: C:\Users\<Your Username>\AppData\Roaming\mpv\scripts\

    Use MPV to Log Timestamps:
        Open your video with MPV.
        Press "c" to toggle cut mode on or off.
        When cut mode is on, use "a" to log start and end timestamps.
		
		You can view the cutlist in real-time as you edit the video with MPV. There are a couple of ways to do this on Windows, allowing you to keep the text file open and see the updates without having to close and reopen the file manually. Here is one approach:
Using a Text Editor with Auto-Reload Feature

Some text editors automatically detect changes to a file and reload it, making them ideal for this scenario.
One such editor is Notepad++ - A popular choice that can auto-reload files when they change.

Steps:

    Open the Text File: Open your cutlist.txt file in Notepad++.

    Enable Auto-Reload:
        Go to Settings > Preferences > MISC and check Update silently and Scroll to last line after update.
    
    Edit in MPV: As you mark your cuts in MPV and the cutlist.txt file gets updated, you’ll see the changes reflected in real-time in Notepad++.

#Use Python to convert Timestamps to LosslessCut ".llc" Project File

Steps to Use "mpv_cutlist_to_llc_v1.2.0.py"

    Set Up Your Variables:
        input_filename: The path to your cutlist.txt.
        output_filename: The path where you want to save the .llc file.
        media_filename: The name of the media file that you are editing (e.g., test.mp4).
        start_buffer_time: Number of seconds to add to the start of each segment (float values allowed).
        end_buffer_time: Number of seconds to add to the end of each segment (float values allowed).

    Run the Script:
        Run the script in your command prompt: 
		Go to the folder your script is in, & type "cmd" in the address bar & hit enter.
		paste "python mpv_cutlist_to_llc_v1.2.0.py" in the command prompt window & hit enter.

    Check the .llc File:
        The script will generate a .llc project file with the structure you provided.
        Open this .llc file in LosslessCut.

Using the .llc File in LosslessCut

    Open LosslessCut.
    Go to File > Open Project File.
    Select the .llc file generated by the script.

This approach should allow you to easily convert your cutlist.txt into a LosslessCut project file compatible with the latest versions of the software.