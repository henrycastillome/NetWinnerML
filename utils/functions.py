import pandas as pd

def get_player_stats(player_name, surface, tourney_level, players_stats_average):
    player_stats = players_stats_average[
        (players_stats_average['player_name'] == player_name) &
        (players_stats_average['surface'] == surface) &
        (players_stats_average['tourney_level'] == tourney_level)
    ].copy()

    if player_stats.empty:
        return "Player or conditions not found"
    return player_stats


def data_point(player_name1, player2_name,surface, tourney_level, players_stats_average):
    new_point=pd.DataFrame({
        'player_hand': [get_player_stats]
    })
