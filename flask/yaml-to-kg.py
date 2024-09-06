import yaml
import numpy as np
from scipy.sparse import csr_array

encoding='UTF-8'

def obtain_players_and_clubs_from_yaml(encoding):
    with open("data/player_clubs.yml", encoding=encoding) as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    players = np.array(list(data.keys()))
    clubs = list(data.values())

    return players,clubs


def get_player_club_interacton_matrix(clubs):

    unique_clubs = np.array(list(set([club for row in clubs for club in row])))

    player_club_interactions_matrix = []
    for player_clubs in clubs:
        player_club_interactions = [club in player_clubs for club in unique_clubs]
        player_club_interactions_matrix.append(player_club_interactions)

    return player_club_interactions_matrix

players, clubs = obtain_players_and_clubs_from_yaml(encoding)

player_club_interactions_matrix = get_player_club_interacton_matrix(clubs)


sparse_player_club_interactions_matrix = csr_array(player_club_interactions_matrix)

# players, unique_clubs, sparse_player_club_interactions_matrix

print(sparse_player_club_interactions_matrix[[0], :])

player_indices = sparse_player_club_interactions_matrix[[0], :].indices

print(player_indices)

unique_clubs = np.array(list(set([club for row in clubs for club in row])))

print(unique_clubs[player_indices])

print(players[0])

print(players[0], clubs[0])