def process_notification(data):
    icons = {
        "Sonarr": "3345",
        "Radarr": "48215"
    }
    payload = {
        "repeat": 3,
        "fadeText": 1000
    }
    url = "http://192.168.0.93/api/notify"

    service = data["instanceName"]
    event = data["eventType"]
    message = None

    if "series" in data:
        show = data["series"]["title"]
        episodes = data["episodes"][0]
        episode_num = episodes["episodeNumber"]
        episode_season = episodes["seasonNumber"]
        episode_title = episodes["title"]
        message = f"{event}: {show} - S{episode_season}E{episode_num} - {episode_title}"

    if "movie" in data:
        movie = data["movie"]["title"]
        quality = data["release"]["quality"]
        message = f"{event}: {movie} ({quality})"
    
    payload.update({"text": message, "icon": icons[service]})
    return {"url": url, "payload": payload}
