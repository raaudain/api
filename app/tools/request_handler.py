import requests


def send_request(url, payload=None, headers=None):
    if payload and headers:
        requests.post(url, headers=headers)
    elif payload:
        requests.post(url, json=payload)
    else:
        requests.get(url)
