import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#st.title('NBA Player Stats Explorer')
st.markdown("""
            
# NBA Player Stats Explorer App
            
This app performs simple webscraping of NBA player stats data!
""")

# sidebar
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

# Web scraping of NBA player stats
@st.cache_data              # decorator @st.chache_data to avoid reloading data every time
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)  # use pandas library to read all tables in this url. header argument indicates first row of table in website is the header
    df = html[0] # first table in the website
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes rows with Age = Age cos in some websites, headers may be repeated
    raw = raw.fillna(0) # fill missing values with 0
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

# Converting all column data to str
playerstats['Team'] = playerstats['Team'].astype(str)
playerstats['Pos'] = playerstats['Pos'].astype(str)


# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Team.unique()) 
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Team.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))] # filtering data based on selected team and position
st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team) # display data in table format

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False) # convert dataframe to csv
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True) # display download link. unsafe_allow_html=True to allow html code in markdown

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    
    df_numeric = df_selected_team.select_dtypes(include=[np.number])

    if not df_numeric.empty:
        corr = df_numeric.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        with sns.axes_style("white"):
            f, ax = plt.subplots(figsize=(7, 5))
            ax = sns.heatmap(corr, mask=mask, vmax=1, square=True,  cmap='coolwarm')
        st.pyplot()
    else:
        st.write('No numerical features to plot heatmap')
        

    #df_selected_team.to_csv('output.csv',index=False)
    # df = pd.read_csv('output.csv')