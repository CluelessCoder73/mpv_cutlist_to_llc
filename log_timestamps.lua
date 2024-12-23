local log_file = nil
local is_start = true
local cut_mode_active = false

function toggle_cut_mode()
    cut_mode_active = not cut_mode_active
    if cut_mode_active then
        log_file = io.open("cutlist.txt", "a")
        mp.osd_message("Cut mode: ON")
    else
        if log_file then
            log_file:close()
            log_file = nil
        end
        mp.osd_message("Cut mode: OFF")
    end
end

function log_timestamp()
    if cut_mode_active and log_file then
        local time_pos = mp.get_property_number("time-pos")
        if is_start then
            log_file:write(string.format("{\"start\": %.3f, ", time_pos))
        else
            log_file:write(string.format("\"end\": %.3f},\n", time_pos))
        end
        is_start = not is_start
        log_file:flush()
    end
end

mp.add_key_binding("c", "toggle-cut-mode", toggle_cut_mode)
mp.add_key_binding("a", "log-timestamp", log_timestamp)
