# Data-Science-Projects

This repository contains various Data Science projects, including an **NBA Player Stats Explorer** app built using Python and the Streamlit framework. Below is an explanation of the NBA Player Stats Explorer app, which scrapes and analyzes NBA player statistics from Basketball Reference.

## NBA Player Stats Explorer App

This project is a simple **NBA Player Stats Explorer** built using Python and the Streamlit web app framework. The app allows users to explore NBA player statistics for a given year by scraping data from [Basketball Reference](https://www.basketball-reference.com).

### Features

- **Web Scraping**: The app scrapes player statistics for any NBA season between 1950 and 2020 from the Basketball Reference website.
- **Interactive Filters**: Users can filter players based on the team and position using a sidebar.
- **Data Display**: The filtered data is displayed in a table format for easy exploration.
- **Downloadable Data**: Users can download the filtered player statistics as a CSV file.
- **Correlation Heatmap**: A heatmap is generated to display the intercorrelation between different numerical stats (like points, rebounds, etc.) for the selected players.

### How It Works

#### Web Scraping
The app scrapes data from Basketball Reference for the selected year using the `pandas` library:
- It reads the data from the table on the website using `pd.read_html()`.
- Since some websites might repeat the headers in long tables, the app removes any repeated header rows (where the `'Age'` column contains the string `'Age'`).
- Missing values are replaced with 0 for easier processing.

#### Interactive Features
- **Year Selection**: Users can select the year of NBA statistics from a dropdown menu in the sidebar.
- **Team & Position Filters**: Users can filter players based on their teams (e.g., Lakers, Warriors) and positions (e.g., Guard, Forward).
  
#### Data Display and Download
- The app shows the filtered player data in a table format, including information such as points per game, rebounds, assists, and more.
- A CSV download link is provided so that users can download the filtered dataset for further analysis.

#### Correlation Heatmap
- By clicking the "Intercorrelation Heatmap" button, the app generates a heatmap that shows the correlation between different numerical stats (e.g., points, assists, rebounds).
- The heatmap is generated using Seaborn's `heatmap()` function, with a `coolwarm` colormap to visualize positive and negative correlations.



