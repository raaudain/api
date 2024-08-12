from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import RedirectResponse, FileResponse
from .tools import send_request, process_notification, set_clock_mode, FileHandler


app = FastAPI()

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

@app.post("/notify")
async def notify_clock(request: Request):
    """Processes post request and sends data to pixel clock as notification"""
    data = await request.json()
    processed_notification = process_notification(data)
    url = processed_notification["url"]
    payload = processed_notification["payload"]
    send_request(url, payload)

    # This request updates media library
    event = process_notification["event"]
    if event.lower() == "download":
        headers = {"X-Emby-Token": ""}
        scan_library_endpoint = "http://localhost:8096/Library/Refresh"
        send_request(scan_library_endpoint, headers=headers, payload={})

@app.get("/set_clock_mode")
def change_clock_mode():
    """Changes pixel clocks setting's settings from day mode to night mode and vice versa"""
    settings = set_clock_mode()
    url = settings["url"]
    payload = settings["payload"]
    send_request(url, payload)

@app.get("/ytd/{video_id}")
def download_video(video_id, background_tasks: BackgroundTasks):
    """Downloads YouTube videos"""
    fh = FileHandler()
    fh.download_and_convert_video(video_id)
    video_file = fh.get_file()
    background_tasks.add_task(fh.clean_up)
    return FileResponse(video_file, media_type="video/mkv", filename=video_file)
