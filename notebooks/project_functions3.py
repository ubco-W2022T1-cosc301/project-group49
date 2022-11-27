import pandas as pd

# Method Chain 1 (Load data, drop na rows, drop unneeded columns)
def load_and_process(filePath):
    unneededColumns = ['Stage', 'Win conditions', 'Half-time Home Goals', 'Half-time Away Goals', 'Referee', 'Assistant 1', 'Assistant 2', 'RoundID', 'MatchID', 'Home Team Initials', 'Away Team Initials', 'Datetime', 'Stadium', 'City'] 
    df1 = (
        pd.read_csv("../data/raw/WorldCupMatches.csv")
        .dropna()
        .drop(unneededColumns, axis=1)
        .sort_values('Attendance', ascending=False)
        .reset_index(drop=True)
    )
    
    
# Method Chain 2 (adding column with total goals) 
def total_attendance (row):
    total_goals= cleanData['Home Team Goals'] + cleanData['Away Team Goals']    
    
    df1['Total Goals'] = (
        df1
        .apply(lambda row: total_attendance(row), axis=1)
    )
    return df1

# Method Chain 3 (dropping all rows where year != 2014)
def final_data(row):
    unneededRows = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010]
    
    df1 = (
        df1
        .drop(cleanData["Year"].isin(unneededData))
    )
    return df1