import json
from nba_video import download_nba_video

with open('playDict.json', 'r') as file:
    playDict = json.load(file)

games_downloaded = 0
for game in playDict:

    if(games_downloaded>=10):
        break

    actions = playDict[game]["game"]["actions"]
    print(f"game#: {game}")

    for action in actions:
        action_type = action["actionType"]
        if action_type=="Missed Shot" or action_type =="Made Shot":
            event_id = action["actionNumber"]
            date = '2024/03/14'

            url = download_nba_video(game, event_id, date)
            if(url):
                print("Video downloaded successfully. URL:", url)
                games_downloaded+=1

    break
