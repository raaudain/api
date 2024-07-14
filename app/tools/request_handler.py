import requests


def send_request(url, payload=None):
    requests.post(url, json=payload) if payload else requests.get(url)
