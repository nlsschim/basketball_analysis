import basketball_analysis
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from basketball_analysis.players_and_teams import players
from basketball_analysis.stat_calcs.scoring_stats import points_per_game

data_path = '/Users/nelsschimek/Documents/codeProjects/basketball_analysis/wehoop-wnba-data/wnba/player_box/csv/'
# file_list = os.listdir(data_path)
# file_list = [file for file in file_list if file.endswith('.csv')]
# print(file_list)

file_list = [
    'player_box_2004.csv','player_box_2003.csv',
    'player_box_2005.csv',
    'player_box_2006.csv',
    'player_box_2007.csv',
    'player_box_2008.csv',
    'player_box_2009.csv',
    'player_box_2010.csv',
    'player_box_2011.csv',
    'player_box_2012.csv',
    'player_box_2013.csv',
    'player_box_2014.csv','player_box_2015.csv','player_box_2016.csv','player_box_2017.csv',
    'player_box_2018.csv',
    'player_box_2019.csv',
    'player_box_2020.csv',
    'player_box_2021.csv',
    'player_box_2022.csv',
    'player_box_2023.csv',
    'player_box_2024.csv',


    
]

player_name_list = []
player_season_list = []
player_ppg_list = []
player_ts_list = []

for file in file_list:

    player_box = pd.read_csv(data_path + file)
    player_box = player_box[player_box['season_type'] == 2] # regular season only
    #print(player_box.columns)



    for player in player_box['athlete_display_name'].unique():
        player_data = players.PlayerSingleSeason(box_score_data=player_box, player_name=player)

        if player_data.games_played >= 10:

            fgp = player_data.get_true_shooting_percentage()
            total_points = player_data.points
            games_played = player_data.games_played

            ppg = np.sum(total_points) / len(total_points)
            

            player_name_list.append(player)
            player_season_list.append(player_data.season)
            player_ppg_list.append(ppg)
            player_ts_list.append(fgp)

player_dict = {
    'player_names': player_name_list,
    'player_seasons': player_season_list,
    'player_ppg': player_ppg_list,
    'player_ts': player_ts_list

}

player_data_frame = pd.DataFrame(player_dict)

print(player_data_frame)

player_data_frame.to_csv(data_path + 'all_player_scoring_data.csv')