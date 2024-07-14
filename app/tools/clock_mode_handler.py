from datetime import datetime, time
from pytz import timezone


def set_clock_mode():
    url = "http://192.168.0.93/api/settings"
    payload = { 
        "WD": False, 
        "TIME_COL": [255,0,0], 
        "TMODE": 0, 
        "BRI": 1,  
        "ABRI": False, 
        "ATRANS": False 
    }

    current_timezone = timezone("America/Los_Angeles")
    current_time = datetime.now(current_timezone)
    start_day_mode =  time(hour=8, minute=0, second=0)
    end_day_mode = time(hour=21, minute=59, second=59)

    if start_day_mode <= current_time.time() <= end_day_mode:
        payload.update({
            "WD": True, 
            "TIME_COL": 16777215, 
            "TMODE": 1,
            "ABRI": True, 
            "ATRANS": True
        })

    return {"url": url, "payload": payload}