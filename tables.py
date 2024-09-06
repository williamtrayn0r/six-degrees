import pandas as pd
import numpy as np
import yaml
import requests
from io import StringIO


wikipedia_base_link = 'https://en.wikipedia.org/wiki'
encoding='UTF-8'


def get_player_unique_teams(player_name):
    player_name = player_name.replace(' ', '_')

    player_url = f"{wikipedia_base_link}/{player_name}"

    print(player_url)

    r = requests.get(player_url)
    website = StringIO(r.text.encode(encoding).decode(encoding))

    try:
        tables=pd.read_html(website, encoding='UTF-8')

        df = tables[0]
        df = df.fillna('')

        first_row = int(df.loc[df[0].str.contains('Senior career')].index[0])
        last_row = int(df.loc[df[0].str.contains('International career')].index[0])

        career_df = df.iloc[first_row+1:last_row, :]

        career_df.columns = career_df.iloc[0]
        career_df = career_df[1:]

        was_loan = career_df['Team'].str.contains('loan')
        career_df_minus_loan = career_df[~was_loan]

        unique_teams = list(career_df_minus_loan['Team'].unique())

        unique_teams[:] = [x for x in unique_teams if x]


        return unique_teams
    
    except Exception as e:
        print(e)
        return None
    
def get_players_clubs_to_yml():

    players_file = open('players.txt', 'r', encoding=encoding)
    players = players_file.read().split('\n')

    players_dict = {}

    for player in players:
        unique_teams = get_player_unique_teams(player)
        print(type(unique_teams))
        if type(unique_teams) == type([]):
            
            players_dict[player] = unique_teams
            print(unique_teams)
            
    with open('player_clubs.yaml', 'w+', encoding=encoding) as f:
        yaml.dump(players_dict, f)

if __name__=='__main__':

    get_players_clubs_to_yml()
