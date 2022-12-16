import flask
import requests
from urllib import parse
import pprint
pp = pprint.PrettyPrinter(indent=4)

api_key = 'RGAPI-1e6e1bf0-0854-466f-a187-2340a819319c'
request_header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,es;q=0.7",
                    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://developer.riotgames.com",
                    "X-Riot-Token": api_key
                }

def summoner_v5_by_summoner_name(summonerName):
    encodingSummonerName = parse.quote(summonerName)
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{encodingSummonerName}"
    return requests.get(url, headers=request_header).json()
#소환사의 이름으로 정보 출력
pp.pprint(summoner_v5_by_summoner_name("d1spel"))

#여기서 json값에서 puuid를 때옴
#puuid로 /lol/match/v5/matches/by-puuid/{puuid}/ids 요청해서 30게임? 50게임? 반복문을 돌려서 배열에 matchid 넣기
#/lol/match/v5/matches/{matchId}에 반복문을 돌려 matchid를 차례로 넣은후 반환되는 json 값에 장로용 데이터를 빼옴
#/lol/match/v5/matches/{matchId}/timeline에서 반복문을 돌려 matchid를 차례로 넣은후 용 상태를 확인함
#마지막으로 index값에 따라 승패로 승률을 조합해 return함