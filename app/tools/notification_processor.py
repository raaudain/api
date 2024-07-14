BASE_URL = "http://192.168.0.93/api"

def process_notification(data):
    icons = {
        "Sonarr": "3345",
        "Radarr": "48215"
    }
    url = BASE_URL + "/notify"
    payload = {"repeat": 5}

    if "series" in data:
        service = data["instanceName"]
        show = data["series"]["title"]
        episodes = data["episodes"][0]
        episode_num = episodes["episodeNumber"]
        episode_season = episodes["seasonNumber"]
        episode_title = episodes["title"]
        event = data["eventType"]
        message = f"{event}: {show} - S{episode_season}E{episode_num} - {episode_title}"
        
        payload.update({"text": message, "icon": icons[service]})

    if "movie" in data:
        service = data["instanceName"]
        movie = data["movie"]["title"]
        event = data["eventType"]
        quality = data["release"]["quality"]
        message = f"{event}: {movie} ({quality})"
    
        payload.update({"text": message, "icon": icons[service]})

    return {"url": url, "payload": payload}