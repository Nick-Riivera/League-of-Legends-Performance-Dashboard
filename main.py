import requests
import csv

API_KEY = 'API_KEY_HERE'

# Gets Users PUUID Given Game Name and Tag Line
def get_puuid(game_name,tag_line):
    url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
    headers = {
        'X-Riot-Token' : API_KEY
    }

    # Gets API Response
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        puuid = data.get('puuid')
        return puuid
    else:
        print(response.json())
        return None


# Gets Matches Given PUUID
def get_matches(puuid):
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=99'
    headers = {
        'X-Riot-Token' : API_KEY
    }

    # Gets API Response
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        match_ids = response.json()
        return match_ids
    else:
        print(response.json())
        return None
    

# Match Results
def get_match_results(match_id):
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}'
    headers = {
        'X-Riot-Token' : API_KEY
    }
    
    # Gets API Response
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        match_data = response.json()
        return match_data
    else:
        print(response.json())
        return None


# Gets data from match  
def get_player_data(match_data,puuid,csv_data):
    if match_data:
        participants = match_data.get('info', {}).get('participants', [])
        for player in participants:
            if player.get('puuid') == puuid:
                game_duration_seconds = match_data.get('info', {}).get('gameDuration')
                minutes = game_duration_seconds // 60 
                seconds = game_duration_seconds % 60

                # Dictionary for the match's data
                match_info = {
                    'Game Duration': f"{minutes}:{seconds:02d}",
                    'Game Mode': match_data.get('info', {}).get('gameMode'),
                    'Champion': player.get('championName'),
                    'Kills': player.get('kills'),
                    'Deaths': player.get('deaths'),
                    'Assists': player.get('assists'),
                    'Lane': player.get('lane'),
                    'Gold Earned': player.get('goldEarned'),
                    'Damage Dealt to Objectives': player.get('damageDealtToObjectives'),
                    'Total Damage Dealt': player.get('totalDamageDealt'),
                    'Total Damage Dealt to Champions': player.get('totalDamageDealtToChampions'),
                    'Total Damage Taken': player.get('totalDamageTaken'),
                    'Total Minions Killed': player.get('totalMinionsKilled'),
                    'Physical Damage Dealt': player.get('physicalDamageDealt'),
                    'Magic Damage Dealt': player.get('magicDamageDealt'),
                    'Riot ID Game Name': player.get('riotIdGameName'),
                    'Win': player.get('win')
                }

                # Append match_info to the csv_data list
                csv_data.append(match_info)
                break
    else:
        print("No Data Available")
        
def write_to_csv(csv_data, filename='data.csv'):
    if not csv_data:
        print("No data to write to CSV.")
        return
    
    with open(filename, mode='w', newline='') as file:
        # Get headers from the first match's data
        fieldnames = csv_data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader() 
        writer.writerows(csv_data)

if __name__ == '__main__':
    game_name = input("Enter Riot Game Name: ")
    tag_line = input("Enter Riot Tag Line: ")

    puuid = get_puuid(game_name, tag_line)

    if puuid: 
        matches = get_matches(puuid)
        csv_data = []
        
        # Fetch each match's details and then get player data
        for match_id in matches:
            match_data = get_match_results(match_id)  # Fetch match data
            if match_data:  # Check if match data was retrieved successfully
                get_player_data(match_data, puuid, csv_data)
                print(f'Adding match: {match_id}')
        print("Finished Importing Data")
        write_to_csv(csv_data)
        
