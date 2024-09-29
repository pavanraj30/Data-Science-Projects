# Data-Science-Projects

This repository contains various Data Science projects, including an **NBA Player Stats Explorer** app built using Python and the Streamlit framework. Below is an explanation of the NBA Player Stats Explorer app, which scrapes and analyzes NBA player statistics from Basketball Reference.

## Simple Stock Price App

This is a **Simple Stock Price App** built using Python and Streamlit. The app fetches historical stock data for Google (Alphabet Inc.) using the `yfinance` library and displays the **closing price** and **trading volume** over time.

### Features

- **Stock Data Fetching**: The app uses the `yfinance` library to retrieve historical stock data for Google (GOOGL).
- **Date Range**: The app fetches stock data from May 31, 2010, to May 31, 2020.
- **Line Charts**: The app displays interactive line charts showing:
  - **Closing Price**: A time series of Google’s closing stock price.
  - **Volume**: A time series of the trading volume for the stock.

### Future Improvements

- Add options for users to select different stocks.
- Allow customization of the date range for the stock data.
- Add additional financial metrics like moving averages or stock performance comparisons.

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

### How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/pavanraj30/Data-Science-Projects.git
   cd Data-Science-Projects
2. Install the required dependencies:
   pip3 install streamlit pandas seaborn matplotlib numpy
3. Run the app:
   streamlit run app.py
4. Open your browser and go to the local address shown (usually http://localhost:8501).



