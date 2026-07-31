def change(string_time):
    return int(string_time[0:2]) * 60 + int(string_time[3:5])

def solution(video_len, pos, op_start, op_end, commands):
    
    int_v = change(video_len)
    int_p = change(pos)
    int_s = change(op_start)
    int_e = change(op_end)
    
    for command in commands:
        
        if int_s <= int_p <= int_e:
            int_p = int_e
        
        if command == "prev":
            int_p = max(int_p - 10, 0)
        
        elif command == "next":
            int_p = min(int_p + 10, int_v)
    
    if int_s <= int_p <= int_e:
        int_p = int_e
    
    return "{:02d}:{:02d}".format(int_p // 60, int_p % 60)