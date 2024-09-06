import yaml
import numpy as np
import networkx as nx

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

def create_graph_from_players_and_clubs(players, clubs):
    assert len(players) == len(clubs)

    G = nx.Graph() 

    for i, player in enumerate(players):
        print(player)
        for club in clubs[i]:
            G.add_edge(player, club)
            
    return G

if __name__=='__main__':

    players, clubs = obtain_players_and_clubs_from_yaml(encoding)

    G = create_graph_from_players_and_clubs(players, clubs)

    print(nx.shortest_path(G, "Zinedine Zidane", "Zlatan Ibrahimović"))

    print(nx.has_path(G, "Zinedine Zidane", "Zlatan Ibrahimović"))

    print("Zlatan Ibrahimović" in G.neighbors("Zinedine Zidane"))

    for path in nx.all_simple_paths(G, "Zinedine Zidane", "Zlatan Ibrahimović", cutoff=5):
        print(path)
        break