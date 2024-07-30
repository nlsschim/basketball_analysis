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

selected_player = st.selectbox(options=np.sort(st.session_state["data"]["athlete_display_name"].unique()), 
                               label="Select a player")

if selected_player:
    player = players.PlayerSingleSeason(st.session_state["data"], selected_player)
else:
    st.write("No player selected.")



stat_to_plot = st.selectbox(options=["Points", "Rebounds", "Assists", "Steals", "Blocks", "Turnovers"],
                            label="Select a stat to plot across the season")

if stat_to_plot == "Points":
    stats_data_frame = pd.DataFrame(columns=["Points"], data=player.points)
elif stat_to_plot == "Rebounds":
    stats_data_frame = pd.DataFrame(columns=["Rebounds"], data=player.total_rebounds)
elif stat_to_plot == "Assists":
    stats_data_frame = pd.DataFrame(columns=["Assists"], data=player.assists)
elif stat_to_plot == "Steals":
    stats_data_frame = pd.DataFrame(columns=["Steals"], data=player.steals)
elif stat_to_plot == "Blocks":
    stats_data_frame = pd.DataFrame(columns=["Blocks"], data=player.blocks)
elif stat_to_plot == "Turnovers":
    stats_data_frame = pd.DataFrame(columns=["Turnovers"], data=player.turnovers)


    
alt_chart = alt.Chart(stats_data_frame).mark_bar().encode(
    alt.X(f"{stat_to_plot}:Q", bin=True),
    y="count()",
)

st.altair_chart(alt_chart)
    