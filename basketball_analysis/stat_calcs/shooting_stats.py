"""
This module will contain functions that calculate shooting statistics for players.
Descriptions of each statistic can be found in the docstrings of each function.
"""


def effective_field_goal_percentage(fgm, fga, three_p_fgm):
    """
    Calculate the effective field goal percentage (eFG%) for a player.

    eFG% = (FGM + 0.5 * 3P_FGM) / FGA

    Parameters:
    fgm (int): The number of field goals made by the player.
    fga (int): The number of field goals attempted by the player.
    three_p_fgm (int): The number of three-point field goals made by the player.

    Returns:
    float: The effective field goal percentage for the player.
    """
    return (fgm + 0.5 * three_p_fgm) / fga


def field_goal_percentage(fgm, fga):
    """
    Calculate the field goal percentage (FG%) for a player.

    FG% = FGM / FGA

    Parameters:
    fgm (int): The number of field goals made by the player.
    fga (int): The number of field goals attempted by the player.

    Returns:
    float: The field goal percentage for the player.
    """
    return fgm / fga


def true_shooting_percentage(pts, fga, fta):
    """
    Calculate the true shooting percentage (TS%) for a player.

    TS% = PTS / (2 * (FGA + 0.44 * FTA))

    Parameters:
    pts (int): The total points scored by the player.
    fga (int): The number of field goals attempted by the player.
    fta (int): The number of free throws attempted by the player.

    Returns:
    float: The true shooting percentage for the player.
    """
    return pts / (2 * (fga + 0.44 * fta))


def points_per_possession(pts, fga, fta, tov):
    """
    Calculate the points per possession (PPP) for a player.

    PPP = PTS / POSS

    Parameters:
    pts (int): The total points scored by the player.
    fga (int): The number of field goals attempted by the player.
    fta (int): The number of free throws attempted by the player.
    tov (int): The number of turnovers committed by the player.

    Returns:
    float: The points per possession for the player.
    """

    poss = fga + 0.44 * fta + tov


    return pts / poss
