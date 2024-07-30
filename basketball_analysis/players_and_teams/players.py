# Module for player class

import pandas as pd
import numpy as np
from basketball_analysis.stat_calcs.shooting_stats import (
    effective_field_goal_percentage,
    field_goal_percentage,
    true_shooting_percentage,
    points_per_possession,
)


class PlayerSingleSeason:
    """
    Represents a basketball player.

    Attributes:
        name (str): The name of the player.
    """

    def __init__(self, box_score_data, player_name):
        self.name = None
        self.player_id = None
        self.position = None
        self.season = None
        self.team = None
        self.minutes = None
        self.games_played = None
        self.field_goals_made = None
        self.field_goals_attempted = None
        self.three_point_field_goals_made = None
        self.three_point_field_goals_attempted = None
        self.free_throws_made = None
        self.free_throws_attempted = None
        self.points = None
        self.offensive_rebounds = None
        self.defensive_rebounds = None
        self.total_rebounds = None
        self.assists = None
        self.steals = None
        self.blocks = None
        self.turnovers = None
        self.personal_fouls = None
        self.plus_minus = None
        self.games_started = None
        self.wins_losses = None
        self.team_scores = None

        df = box_score_data.fillna(0)

        player_data = df[
            df["athlete_display_name"] == player_name
        ]  # assuming the column for player names is 'name'
        if not player_data.empty:
            self.name = player_data.iloc[0]["athlete_display_name"]
            self.player_id = player_data.iloc[0]["athlete_id"]
            self.position = player_data.iloc[0]["athlete_position_abbreviation"]
            self.season = player_data.iloc[0]["season"]
            self.team = player_data.iloc[0]["team_name"]
            self.minutes = np.array(player_data["minutes"])
            self.games_played = player_data[
                "active"
            ].sum()  # assuming the column for games played is 'active
            self.field_goals_made = np.array(player_data["field_goals_made"])
            self.field_goals_attempted = np.array(player_data["field_goals_attempted"])
            self.three_point_field_goals_made = np.array(
                player_data["three_point_field_goals_made"]
            )
            self.three_point_field_goals_attempted = np.array(
                player_data["three_point_field_goals_attempted"]
            )
            self.free_throws_made = np.array(player_data["free_throws_made"])
            self.free_throws_attempted = np.array(player_data["free_throws_attempted"])
            self.points = np.array(player_data["points"])
            self.offensive_rebounds = np.array(player_data["offensive_rebounds"])
            self.defensive_rebounds = np.array(player_data["defensive_rebounds"])
            self.total_rebounds = np.array(player_data["rebounds"])
            self.assists = np.array(player_data["assists"])
            self.steals = np.array(player_data["steals"])
            self.blocks = np.array(player_data["blocks"])
            self.turnovers = np.array(player_data["turnovers"])
            self.personal_fouls = np.array(player_data["fouls"])
            self.plus_minus = np.array(player_data["plus_minus"])
            self.games_started = player_data["starter"].sum()
            self.wins_losses = player_data["team_winner"]
            self.team_scores = np.array(player_data["team_score"])
        else:
            raise ValueError("Player not found in the dataset")

    def get_true_shooting_percentage(self):
        """
        Calculate the true shooting percentage (TS%) for the player.

        TS% = PTS / (2 * (FGA + 0.44 * FTA))

        Returns:
        float: The true shooting percentage for the player.
        """

        points_sum = np.nan_to_num(self.points, 0).sum()
        fga_sum = np.nan_to_num(self.field_goals_attempted, 0).sum()
        fta_sum = np.nan_to_num(self.free_throws_attempted, 0).sum()
        return true_shooting_percentage(
            points_sum, fga_sum, fta_sum
        )

    def get_effective_field_goal_percentage(self):
        """
        Calculate the effective field goal percentage (eFG%) for the player.
        """

        fgm_sum = np.nan_to_num(self.field_goals_made, 0).sum()
        fga_sum = np.nan_to_num(self.field_goals_attempted, 0).sum()
        three_p_fgm_sum = np.nan_to_num(self.three_point_field_goals_made, 0).sum()
        return effective_field_goal_percentage(
            fgm_sum,
            fga_sum,
            three_p_fgm_sum 
        )

    def get_field_goal_percentage(self):
        """
        Calculate the field goal percentage (FG%) for the player.
        """

        fgm_sum = np.nan_to_num(self.field_goals_made, 0).sum()
        fga_sum = np.nan_to_num(self.field_goals_attempted, 0).sum()
        return field_goal_percentage(
            fgm_sum,
            fga_sum
        )

    def get_points_per_possession(self):
        """
        Calculate the points per possession (PPP) for the player.
        """

        points_sum = np.nan_to_num(self.points, 0).sum()
        fga_sum = np.nan_to_num(self.field_goals_attempted, 0).sum()
        fta_sum = np.nan_to_num(self.free_throws_attempted, 0).sum()
        tov_sum = np.nan_to_num(self.turnovers, 0).sum()
        return points_per_possession(
            points_sum,
            fga_sum,
            fta_sum,
            tov_sum
        )
