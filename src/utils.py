import pandas as pd

player_stats_average_df= pd.read_csv('../data/players_stats_average.csv')
player_basic_info_df = pd.read_csv('../data/player_basic_info.csv')
def get_player_stats(player_name, surface, tourney_level):
    player_stats = player_stats_average_df[
        (player_stats_average_df['player_name'] == player_name) &
        (player_stats_average_df['surface'] == surface) &
        (player_stats_average_df['tourney_level'] == tourney_level)
    ]

    if player_stats.empty:
        return "Player or conditions not found"
    return player_stats



def get_player_basic_info(player_name):
    player_info = player_basic_info_df[
        (player_basic_info_df['player_name'] == player_name)
    ]

    if player_info.empty:
        return "Player not found"
    return player_info


def get_player_stats_and_info(player, surface, tourney_level, player_age):

    try:
        player_stats = get_player_stats(player, surface, tourney_level)
        player_basic_info = get_player_basic_info(player)
    except Exception as e:
        print(f"Error fetching data for {player}:{e}")

        return (
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', player_age
        ) 
    
    return (
        player_stats['avg_ace'].values[0].astype(int),
        player_stats['avg_df'].values[0].astype(int),
        player_stats['avg_svpt'].values[0].astype(int),
        player_stats['avg_1stIn'].values[0].astype(int),
        player_stats['avg_1stWon'].values[0].astype(int),
        player_stats['avg_2ndWon'].values[0].astype(int),
        player_stats['avg_SvGms'].values[0].astype(int),
        player_stats['avg_bpSaved'].values[0].astype(int),
        player_stats['avg_bpFaced'].values[0].astype(int),
        player_basic_info['player_ht'].values[0].astype(int),
        player_basic_info['player_hand'].values[0],
        player_age
    )


def data_point(player1_info_dict, player2_info_dict, match_info_dict):
    player1 = player1_info_dict['player1']
    player2 = player2_info_dict['player2']
    player1_age = player1_info_dict['player1_age']
    player2_age = player2_info_dict['player2_age']
    rank_player1 = player1_info_dict['player1_rank']
    rank_player2 = player2_info_dict['player2_rank']
    surface = match_info_dict['surface']
    tourney_level = match_info_dict['tourney_level']
    best_of = match_info_dict['best_of']


    try:
        (
            player1_avg_ace, player1_avg_df, player1_avg_svpt,
            player1_avg_1stIn, player1_avg_1stWon, player1_avg_2ndWon,
            player1_avg_SvGms, player1_avg_bpSaved, player1_avg_bpFaced,
            player1_ht, player1_hand, _
        ) = get_player_stats_and_info(player1, surface, tourney_level, player1_age)

        (
            player2_avg_ace, player2_avg_df, player2_avg_svpt,
            player2_avg_1stIn, player2_avg_1stWon, player2_avg_2ndWon,
            player2_avg_SvGms, player2_avg_bpSaved, player2_avg_bpFaced,
            player2_ht, player2_hand, _
        ) = get_player_stats_and_info(player2, surface, tourney_level, player2_age)

        data_point = pd.DataFrame({
            'player_hand': [player1_hand, player2_hand],
            'player_ht': [player1_ht, player2_ht],
            'player_age': [player1_age, player2_age],
            'ace': [player1_avg_ace, player2_avg_ace],
            'df': [player1_avg_df, player2_avg_df],
            'svpt': [player1_avg_svpt, player2_avg_svpt],
            '1stIn': [player1_avg_1stIn, player2_avg_1stIn],
            '1stWon': [player1_avg_1stWon, player2_avg_1stWon],
            '2ndWon': [player1_avg_2ndWon, player2_avg_2ndWon],
            'SvGms': [player1_avg_SvGms, player2_avg_SvGms],
            'bpSaved': [player1_avg_bpSaved, player2_avg_bpSaved],
            'bpFaced': [player1_avg_bpFaced, player2_avg_bpFaced],
            'rank': [rank_player1, rank_player2],
            'opponent_rank': [rank_player2, rank_player1],
            'surface': [surface, surface],
            'tourney_level': [tourney_level, tourney_level],
            'best_of': [best_of, best_of]
        })

    

    except Exception as e:
        print(f"Error fetching data for {player1} vs {player2}:{e}")

        return None

    return data_point

