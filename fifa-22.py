import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
import seaborn as sns
sns.set_theme(style="dark")

df_fifa = pd.read_csv("players_22.csv")

def run():
    st.set_page_config(layout="wide")
    st.header("FIFA 22 Player comparator")
    st.write("Welcome to the FIFA 22 Player comparator")
    st.write("Use the prompts below to select players you would like to compare")
    gk_comparison = st.checkbox("Are you comparing GK?")
    if gk_comparison == True:
        football = df_fifa[df_fifa["player_positions"].str.strip() == "GK"]
        gk_football = football[['short_name', 'league_name', 'club_name',
                                'goalkeeping_diving', 'goalkeeping_handling',
                                'goalkeeping_kicking','goalkeeping_positioning',
                                'goalkeeping_reflexes','goalkeeping_speed']]

        st.subheader("Use the options below to select the first player")
        league_name = list(gk_football["league_name"].unique())
        league = st.selectbox('League Selector', league_name)

        team_fifa = gk_football[gk_football["league_name"] == league]
        team_name = list(team_fifa["club_name"].unique())
        team = st.selectbox('Team Selector', team_name)

        player_fifa = team_fifa[team_fifa["club_name"] == team]
        player_name = list(player_fifa["short_name"].unique())
        player = st.selectbox('Player Selector', player_name)

        st.subheader("Use the options below to select the second player")
        league_name2 = list(gk_football["league_name"].unique())
        league2 = st.selectbox('League Selector 2', league_name2)

        team_fifa2 = gk_football[gk_football["league_name"] == league2]
        team_name2 = list(team_fifa2["club_name"].unique())
        team2 = st.selectbox('Team Selector 2', team_name2)

        player_fifa2 = team_fifa2[team_fifa2["club_name"] == team2]
        player_name2 = list(player_fifa2["short_name"].unique())
        player2 = st.selectbox('Player Selector 2', player_name2)

        st.subheader("Here is a chart comparing the two players")
        categories = ['diving', 'handling', 'kicking', 
                      'positioning', 'reflexes', 'speed']
        N = len(categories)
        #categories = [*categories, categories[0]]

        index1 = football.index[(gk_football['short_name'] == player)]
        index2 = football.index[(gk_football['short_name'] == player2)]
        play_one = football.loc[index1, ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
                                         'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']].values.flatten().tolist()
        play_two = football.loc[index2, ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
                                         'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']].values.flatten().tolist()
        player_one = [*play_one, play_one[0]]
        player_two = [*play_two, play_two[0]]
        # label_loc = np.linspace(start=0, stop=2*np.pi, num=len(player_one))
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]
        #fig, ax = plt.subplots(figsize=(16, 8))
        fig = plt.figure(figsize=(20, 10))
        ax = plt.subplot(polar=True)
        #ax.subplot(polar=True)
        plt.xticks(angles[:-1], categories, color='grey', size=11)
        ax.set_rlabel_position(0)
        plt.yticks([20, 40, 60, 80], ["20", "40", "60", "80"],
                   color="grey", size=7)
        plt.ylim(0, 100)
        ax.plot(angles, player_one, label=player)
        ax.plot(angles, player_two, label=player2)
        #lines, labels = ax.thetagrids(np.degrees(label_loc), labels=categories)
        ax.legend(loc="upper left", frameon=False)
        ax.set_title("FIFA 22 Players' comparison", fontsize=16)
        buf = BytesIO()
        fig.savefig(buf, format="png")
        #image_width = st.number_input("Image Width", 1, 2000, 700)
        #use_column_width = st.checkbox("Use Column Width")
        st.image(buf, width=1000, use_column_width=True)
        #st.pyplot(fig)
    else: 
        football = df_fifa[['short_name', 'league_name', 'club_name', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
        football = football.dropna()
        st.subheader("Use the options below to select the first player")
        league_name = list(football["league_name"].unique())
        league = st.selectbox('League Selector', league_name)
    
        team_fifa = football[football["league_name"] == league]
        team_name = list(team_fifa["club_name"].unique())
        team = st.selectbox('Team Selector', team_name)

        player_fifa = team_fifa[team_fifa["club_name"] == team]
        player_name = list(player_fifa["short_name"].unique())
        player = st.selectbox('Player Selector', player_name)

        st.subheader("Use the options below to select the second player")
        league_name2 = list(football["league_name"].unique())
        league2 = st.selectbox('League Selector 2', league_name2)

        team_fifa2 = football[football["league_name"] == league2]
        team_name2 = list(team_fifa2["club_name"].unique())
        team2 = st.selectbox('Team Selector 2', team_name2)

        player_fifa2 = team_fifa2[team_fifa2["club_name"] == team2]
        player_name2 = list(player_fifa2["short_name"].unique())
        player2 = st.selectbox('Player Selector 2', player_name2)

        st.subheader("Here is a chart comparing the two players")
        categories = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
        N = len(categories)
        #categories = [*categories, categories[0]]

        index1 = football.index[(football['short_name'] == player)]
        index2 = football.index[(football['short_name'] == player2)]
        play_one = football.loc[index1, ['pace', 'shooting', 'passing',
                                         'dribbling', 'defending', 'physic']].values.flatten().tolist()
        play_two = football.loc[index2, ['pace', 'shooting', 'passing',
                                         'dribbling', 'defending', 'physic']].values.flatten().tolist()
        player_one = [*play_one, play_one[0]]
        player_two = [*play_two, play_two[0]]
        # label_loc = np.linspace(start=0, stop=2*np.pi, num=len(player_one))
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]
        #fig, ax = plt.subplots(figsize=(16, 8))
        fig = plt.figure(figsize=(20, 10))
        ax = plt.subplot(polar=True)
        #ax.subplot(polar=True)
        plt.xticks(angles[:-1], categories, color='grey', size=11)
        ax.set_rlabel_position(0)
        plt.yticks([20, 40, 60, 80], ["20", "40", "60", "80"], color="grey", size=7)
        plt.ylim(0, 100)
        ax.plot(angles, player_one, label=player)
        ax.plot(angles, player_two, label=player2)
        #lines, labels = ax.thetagrids(np.degrees(label_loc), labels=categories)
        ax.legend(loc="upper left", frameon=False)
        ax.set_title("FIFA 22 Players' comparison", fontsize=16)
        buf = BytesIO()
        fig.savefig(buf, format="png")
        #image_width = st.number_input("Image Width", 1, 2000, 700)
        #use_column_width = st.checkbox("Use Column Width")
        st.image(buf, width=1000, use_column_width=True)
        #st.pyplot(fig)
  

if __name__ == '__main__':
    run()