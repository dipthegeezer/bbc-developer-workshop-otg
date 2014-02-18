import requests
from datetime import datetime

def get_json_response(url):
    response = requests.get(url)
    return response.json()

def extract_episode_data(data):
    episode_array = []
    for episode in data["episodes"]:
        episode_list = episode["programme"]["display_titles"]
        #TODO: Implement feature here
        episode_array.append(episode_list)
    final = {'episodes': episode_array}
    return final

def get_barlesque():
    url = "http://www.live.bbc.co.uk/frameworks/barlesque/orb/webservice.json"
    response = get_json_response(url)
    barlesque = response["barlesque"]
    return barlesque

def string_to_datetime(string):
    return datetime.strptime(string,'%Y-%m-%dT%H:%M:%SZ')

def get_online_availability_window(broadcast_date, available_until):
    return str(available_until - broadcast_date)
