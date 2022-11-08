import pandas as pd

def load_and_process(filePath):
   
    # Method Chain 1 (Load data, drop na rows, drop unneeded columns)
    
    # Preparing list needed
    unneededCols = ['Datetime','Stage', 'Stadium', 'City', 'Win conditions', 'Attendance', 'Half-time Home Goals', 'Half-time Away Goals', 'Referee', 'Assistant 1', 'Assistant 2', 'RoundID', 'MatchID', 'Home Team Initials', 'Away Team Initials']
    
    df1 = (
        pd.read_csv("../data/raw/WorldCupMatches.csv")
        .dropna()
        .drop(unneededCols, axis=1)
        .reset_index(drop=True)
    )
    
    # Method Chain 2 (adding column with values for winner) 
    
    # Preparing function needed
    def label_winner (row):
        if row['Home Team Goals'] > row['Away Team Goals']:
            return 1
        if row['Home Team Goals'] < row['Away Team Goals']:
            return 2
        return 0
    
    df1['Winner'] = (
        df1
        .apply (lambda row: label_winner(row), axis=1)
    )
        
    
    return df1