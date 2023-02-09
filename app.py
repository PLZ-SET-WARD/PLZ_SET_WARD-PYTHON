import flask
import requests
from urllib import parse
import pprint
pp = pprint.PrettyPrinter(indent=4)

api_key = 'RGAPI-19d049e3-39a7-4a3b-b966-8d5aa14a224e'
request_header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,es;q=0.7",
                    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://developer.riotgames.com",
                    "X-Riot-Token": api_key
                }

                

def summoner_v4_by_summoner_name(summonerName):
    encodingSummonerName = parse.quote(summonerName)
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{encodingSummonerName}"
    return requests.get(url, headers=request_header).json()
#소환사의 이름으로 정보 출력
r = summoner_v4_by_summoner_name("d1spel")
puuid = r['puuid']
print(puuid)

def matchgame():
    encodingPuuid = parse.quote(puuid)
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=50&api_key={api_key}"
    return requests.get(url, headers=request_header).json()

r = matchgame()
print(r)

matchids = []

def checkgametype(matchid):
    encodingPuuid = parse.quote(puuid)
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchid}?api_key={api_key}"
    return requests.get(url, headers=request_header).json()

for i in range(0, 50) :
  a = checkgametype(r[i])
  if(a["info"]["gameMode"] == "CLASSIC") : 
    matchids.append(r[i])
      

for i in range(0, len(matchids)) : 
  print(matchids[i])

