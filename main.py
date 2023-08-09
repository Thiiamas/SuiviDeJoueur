from utitils import matrixFromListDict
from datetime import datetime
import core
import writer

debugCounter = 0



Ids =""


gameDictList = []
#endpoints
sumonnerEndPoint = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{core.summoner_name}?api_key={core.api_key}"
accountInfos = core.callAPI(sumonnerEndPoint).json()
puuid = accountInfos["puuid"]
hystoryEndPoint = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?api_key={core.api_key}"


#get puuid



matchIds = core.callAPI(hystoryEndPoint)
matchIds = matchIds.json()
for matchId in matchIds:
    matchV5EndPoint = f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={core.api_key}"
    match = core.callAPI(matchV5EndPoint)
    headers = match.headers
    match = match.json()
    gameDict = {}   
    if match["info"]["queueId"] != 420:
        continue
    totalKill = 0
    dateString = headers["Date"]
    date = datetime.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
    formatted_date = date.strftime("%d/%m/%Y")
    gameDict["Date"] = formatted_date
    for participant in match["info"]["participants"]:

        if participant["summonerName"] == "Thiiamas":
            teamId = participant["teamId"]
            gameDict["champion"] = participant["championName"]
            gameDict["kills"] = participant["kills"]
            gameDict["deaths"] = participant["deaths"]
            gameDict["assists"] = participant["assists"]
            gameDict["win"] = "Win" if participant["win"] == True else "Loose"
            gameDict["wardsPlaced"] = participant["wardsPlaced"]
            gameDict["detectorWardsPlaced"] = participant["detectorWardsPlaced"]
            gameDict["SV"] = participant["visionScore"]
            gameDict["totalMinionsKilled"] = participant["totalMinionsKilled"] + participant["neutralMinionsKilled"]
            gameDict["gameDuration"] = int(match["info"]["gameDuration"]/60)
    for participant in match["info"]["participants"]:
        if participant["teamId"] == teamId:
            totalKill += participant["kills"]
    gameDict["totalKill"] = totalKill
    gameDictList.append(gameDict)
    debugCounter += 1

ListofList = matrixFromListDict(gameDictList)
writer.write(ListofList)

exit()


