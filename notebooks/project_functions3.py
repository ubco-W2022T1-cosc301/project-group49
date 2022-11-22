import pandas as pd

def load_and_process(filePath):
   
    # Method Chain 1 (Load data, drop na rows, drop unneeded columns)
    
    # Preparing list needed
    unneededColumns = ['Stage', 'Win conditions', 'Half-time Home Goals', 'Half-time Away Goals', 'Referee', 'Assistant 1', 'Assistant 2', 'RoundID', 'MatchID', 'Home Team Initials', 'Away Team Initials']    
    
    df1 = (
        pd.read_csv("../data/raw/WorldCupMatches.csv")
        .dropna()
        .drop(unneededColumns, axis=1)
        .reset_index(drop=True)
    )
 
# Method Chain 2 (adding column with values for winner) 
    
# Preparing function needed
def total_attendance (row):
    total_goals= cleanData['Home Team Goals'] + cleanData['Away Team Goals']    
    
    df1['Total Goals'] = (
        df1
        .apply (lambda row: total_attendance(row), axis=1)
    )
    return df1