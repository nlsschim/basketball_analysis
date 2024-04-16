"""
The scoring_states module contains functions for calculating 
various scoring statistics for basketball players.
Descriptions of each statistic can be found in the docstrings of each function.
Currently, this include:
- Points per game
- Points per 36 minutes
- Points per 75 possessions
- % of teams points scored
"""

import pandas as pd
import numpy as np


def points_per_game(pts, games_played):
    """
    Calculate the points per game (PPG) for a player.

    PPG = PTS / Games Played

    Parameters:
    pts (int): The total points scored by the player.
    games_played (int): The number of games played by the player.

    Returns:
    float: The points per game for the player.
    """
    return pts / games_played


def points_per_36_minutes(pts, minutes):
    """
    Calculate the points per 36 minutes for a player.

    Points per 36 minutes = (PTS / Minutes) * 36

    Parameters:
    pts (int): The total points scored by the player.
    minutes (int): The total minutes played by the player.

    Returns:
    float: The points per 36 minutes for the player.
    """
    return (pts / minutes) * 36


def points_per_75_possessions(pts, possessions):
    """
    Calculate the points per 75 possessions for a player.

    Points per 75 possessions = (PTS / Possessions) * 75

    Parameters:
    pts (int): The total points scored by the player.
    possessions (int): The total possessions by the player.

    Returns:
    float: The points per 75 possessions for the player.
    """
    return (pts / possessions) * 75


def percentage_of_teams_points_scored(pts, team_pts):
    """
    Calculate the percentage of the team's points scored by a player.

    % of Team's Points Scored = (PTS / Team PTS) * 100

    Parameters:
    pts (int): The total points scored by the player.
    team_pts (int): The total points scored by the team.

    Returns:
    float: The percentage of the team's points scored by the player.
    """
    return (pts / team_pts) * 100


def adjusted_points_per_75():
    pass
