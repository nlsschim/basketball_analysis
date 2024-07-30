import pandas as pd
import streamlit as st
from basketball_analysis.players_and_teams import players, teams
import numpy as np
import altair as alt

# --- page setup ---
st.write("This page is for plotting data.")

if st.session_state["data"] is not None:
    st.write("Here is the data:")
    st.write(st.session_state["data"])

# --- data visualization ---

athletes = [player for player in st.session_state["data"]["athlete_display_name"].unique()]
ts = [players.PlayerSingleSeason(st.session_state["data"], player).get_true_shooting_percentage() for player in athletes]
eff_fgp = [players.PlayerSingleSeason(st.session_state["data"], player).get_effective_field_goal_percentage() for player in athletes]
ppp = [players.PlayerSingleSeason(st.session_state["data"], player).get_points_per_possession() for player in athletes]
ppg = [np.sum(players.PlayerSingleSeason(st.session_state["data"], player).points) / len(players.PlayerSingleSeason(st.session_state["data"], player).points) for player in athletes]

df = pd.DataFrame(columns=["Athlete", "TS%", "PPG", 'effFGP', 'PPP'], data=zip(athletes, ts, ppg, eff_fgp, ppp))


st.write(df)

y_axis_stat = st.selectbox(options=["TS%", "effFGP", "PPP"],
                           label="Select a stat for the y-axis", placeholder="Select a stat")

if y_axis_stat == "TS%":
    base_chart = alt.Chart(df).mark_circle().encode(
        x="PPG",
        y="TS%",
        tooltip=["Athlete", "PPG", "TS%"],
    ).interactive()

    mean_ts = np.mean(df["TS%"])
    mean_rule = alt.Chart(pd.DataFrame({'mean_ts': [mean_ts]})).mark_rule(color='red').encode(
    y='mean_ts:Q')

    alt_chart = base_chart + mean_rule

elif y_axis_stat == "effFGP":
    base_chart = alt.Chart(df).mark_circle().encode(
        x="PPG",
        y="effFGP",
        tooltip=["Athlete", "PPG", "effFGP"],
    ).interactive()

    mean_efffgp = np.mean(df["effFGP"])
    mean_rule = alt.Chart(pd.DataFrame({'mean_efffgp': [mean_efffgp]})).mark_rule(color='red').encode(
    y='mean_efffgp:Q')

    alt_chart = base_chart + mean_rule

elif y_axis_stat == "PPP":
    base_chart = alt.Chart(df).mark_circle().encode(
        x="PPG",
        y="PPP",
        tooltip=["Athlete", "PPG", "PPP"],
    ).interactive()

    mean_ppp = np.mean(df["PPP"])
    mean_rule = alt.Chart(pd.DataFrame({'mean_ppp': [mean_ppp]})).mark_rule(color='red').encode(
    y='mean_ppp:Q')

    alt_chart = base_chart + mean_rule
    
else:
    st.write("No stat selected.")


st.altair_chart(alt_chart, use_container_width=True)

