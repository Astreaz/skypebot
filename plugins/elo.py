#elo http://elophant.com/developers/docs
import urllib2, json, base64

key = "dVEzYTR6U3l5MENQZ3VvMUtDS2Y"
idURL = "http://api.elophant.com/v2/na/summoner/{name}?key={key}"
eloURL = "http://api.elophant.com/v2/na/player_stats/{id}?key={key}"
opener = urllib2.build_opener()

def GetID(user):
	url = idURL.format(name=user, key=base64.b64decode(key + '='))
	data = opener.open(url).read()
	jsonData = json.loads(data)
	return jsonData["data"]["acctId"]

def GetELO(accID):
	url = eloURL.format(id=accID, key=base64.b64decode(key + '='))
	data = opener.open(url)
	jsonData = json.loads(data)
	return jsonData["data"]["playerStatSummaries"]["playerStatSummarySet"][0]["maxRating"]

if __name__ == "__main__":
	print GetID('astreaz')
	print GetELO(33603095)

