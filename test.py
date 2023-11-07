import json

list = []

for i in range(0, 50):
    print(i*1000)

    start = i*1000
    end = start+999

    path = "data/mpd.slice." + str(start) + "-" + str(end) + ".json"
    with open(path) as file:
        data = json.load(file)
        list.append(data["playlists"])

print(len(list))