#elo http://elophant.com/developers/docs
import urllib2, json, base64

key = "dVEzYTR6U3l5MENQZ3VvMUtDS2Y"
apiURL = "http://api.elophant.com/v2/na/in_progress_game_info/{name}?key={key}"
replayURL = "lrf://spectator {ip}:{port} {key} {id} NA1"
ensURL = "http://sonng.es/~brad/ensuna/spectate.php?id={id}"
opener = urllib2.build_opener()

def GetInfo(user):
	try:
		url = apiURL.format(name=user, key=base64.b64decode(key + '='))
		data = opener.open(url).read()
		jsonData = json.loads(data)
		gameId = jsonData['data']['playerCredentials']['gameId']
		serverIp = jsonData['data']['playerCredentials']['observerServerIp']
		serverPort = jsonData['data']['playerCredentials']['observerServerPort']
		serverKey = jsonData['data']['playerCredentials']['observerEncryptionKey']
		return gameId, serverIp, serverPort, serverKey
	except KeyError, HTTPError:
		return None

def GetUrl(user):
	try:
		gameId, serverIp, serverPort, serverKey = GetInfo(str(user))
		replay = replayURL.format(ip=serverIp, port=serverPort, key=serverKey, id=gameId)	#base url
		replay = base64.b64encode(replay)
		replay = ensURL.format(id=replay)
		return replay
	except TypeError:
		return 'No games found for {0}'.format(user)

if __name__ == "__main__":
	import sys
	try:
		print GetUrl(sys.argv[1])
	except IndexError:
		print 'Usage - spectate.py <username>'

