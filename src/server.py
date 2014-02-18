from flask import Flask, jsonify, render_template
import sys

from lib import get_json_response, extract_episode_data, get_barlesque

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the BBC Winter Olympics Content"

@app.route("/service/winterolympics")
def winter_olympic_schedules():
    url = "http://www.bbc.co.uk/programmes/genres/sport/winterolympics/player/episodes.json"
    data = get_json_response(url)
    final = extract_episode_data(data)
    return jsonify(**final)

@app.route("/catchup")
def catchup():
    barlesque = get_barlesque()
    url = "http://www.bbc.co.uk/programmes/genres/sport/winterolympics/player/episodes.json"
    data = get_json_response(url)
    episodes = extract_episode_data(data)["episodes"]
    return render_template("index.html", barlesque=barlesque, episodes=episodes)

if __name__ == "__main__":
    # You can pass the port number as an argument
    try:
        port = int(sys.argv[1])
    except IndexError:
        port = 5000
    except ValueError:
        print "Port argument must be an integer!"
        sys.exit()

    app.run(host="0.0.0.0", port=port, debug=True)

