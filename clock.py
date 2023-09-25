import time
import datetime
import winsound

def focus_timer(hours, minutes):
    total_seconds = (hours * 3600) + (minutes * 60)
    end_time = time.time() + total_seconds

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        remaining_time = str(datetime.timedelta(seconds=remaining_seconds))

        print(f"Remaining Time: {remaining_time}", end="\r", flush=True)
        time.sleep(1)

    print("Focus timer completed!")
    winsound.Beep(1000, 1000)  # 播放提示音

# 设置专注时长为2小时30分钟
focus_timer(2, 30)
