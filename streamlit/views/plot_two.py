import pandas as pd
import streamlit as st
from basketball_analysis.players_and_teams import players, teams
import random
import numpy as np
import altair as alt

# --- page setup ---
st.write("This page is for plotting data.")

if st.session_state["data"] is not None:
    st.write("Here is the data:")
    st.write(st.session_state["data"])

# --- data visualization ---

true_shooting_data = []
for player_name in st.session_state["data"]["athlete_display_name"].unique():
    player = players.PlayerSingleSeason(st.session_state["data"], player_name)
    ts = player.get_true_shooting_percentage()
    true_shooting_data.append({"Player": player_name, "True Shooting Percentage": ts})

points_per_game = []
for player_name in st.session_state["data"]["athlete_display_name"].unique():
    player = players.PlayerSingleSeason(st.session_state["data"], player_name)
    points = player.points
    games_played = player.games_played
    ppg = points / games_played
    points_per_game.append({"Player": player_name, "Points Per Game": ppg})

