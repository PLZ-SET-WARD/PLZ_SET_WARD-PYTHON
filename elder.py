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

def match_v5_get_match_history(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}"
    return requests.get(url, headers=request_header).json()

pp.pprint(match_v5_get_match_history("KR_6150979499"))