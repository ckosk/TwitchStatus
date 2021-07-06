#Initial Design by Vegard Valvik (https://github.com/begs) I have made modifications. Thank you.

import sys, json, requests; 
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except Exception:
    pass

#See if oauth.txt exists
try:
    with open('oauth.txt', 'r') as f:
        oauth = f.read()
	
except FileNotFoundError:
    print("Paste your OAuth (like 'yaxb50....')")
    with open('oauth.txt', 'w') as f:
        f.write (input ())
    with open('oauth.txt', 'r') as f:
        oauth = f.read()

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': '*INSERT CLIENT ID*', #Insert your own, personal, client ID
    'Authorization': 'OAuth ' + oauth,
}
try:
    response = requests.get('https://api.twitch.tv/kraken/streams/followed', headers=headers)
    data = response.json()
    numStreams = len(data['streams'])
except (KeyError, ValueError):
    print("Error: Is OAuth formatted correctly in oauth.txt ?")
    sys.exit(1)

print ("\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80)

for i in range (0, numStreams): 
    channelName = data["streams"][i]["channel"]["name"];
    channelGame = data["streams"][i]["channel"]["game"];
    channelViewers = str(data["streams"][i]["viewers"]);
    streamType = data["streams"][i]["stream_type"];

    #Check if stream is live or displaying a VOD
    if(streamType == "live"):
    	streamType = "";
    else:
    	streamType = "(vodcast)";

    if(len(channelName) > 18):
    	channelName = channelName[:18] + ".."
    if(len(channelGame) > 38):
        channelGame = channelGame[:38] + ".."

    print ("{} {} {} {}".format(
	channelName.ljust(20),
	channelGame.ljust(40), 
	channelViewers.ljust(8), 
	streamType
    ))

    if (i == numStreams-1):
        print ('-'*80)
