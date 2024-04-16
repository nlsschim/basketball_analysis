# Module for doing calculations related to plus minus


def relative_plus_minus(player, team):
    """
    Calculates the relative plus minus of a player on a team. The relative plus minus is the difference between the player's plus minus and the team's average plus minus.

    Args:
        player (Player): The player to calculate the relative plus minus for.
        team (Team): The team the player is on.

    Returns:
        float: The relative plus minus of the player.
    """

    return player.plus_minus - team.average_plus_minus
