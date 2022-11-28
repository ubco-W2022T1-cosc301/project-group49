#Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as plt

def load_and_process1(url_or_path_to_csv_file):

    # Method Chain 1 (Load data)
    df1 = pd.read_csv(url_or_path_to_csv_file)

    # Method Chain 2 (Drop unneccessary columns like the Attendance,
    #Check if the winners are a home team(to make sure that every winner counted is a visiting team);
    
    #Preparing the lists and functions needed
    DeleteList=['Runners-Up','Third','Fourth','QualifiedTeams','MatchesPlayed','Attendance',"GoalsScored"]
    
    def func(row):
        if row['Country'] in row['Winner']:
            val = False
        else:
            val = True
        return val
    
    #Chaining
    df2=df1.drop(
        DeleteList, axis=1
    ).assign(
        AwayTeam = df1.apply(func, axis=1)
    )
    
    #Method Chain 3 (Delete all home teams;
    #Delete the Hosting Countries to get a list of winners since it isn't important for our analysis
    #Drop the original index)
    df3 = df2.drop(
        df2[df2["AwayTeam"] == False].index
    ).drop(["AwayTeam","Country"], axis=1
          ).reset_index(
    ).drop("index", axis=1
          )

    #Turn "Germany FR" to "Germany" to simplify the process (Sorry for historians striving for accuracy, but my sleep is more important;
    df3.loc[df3['Winner'] == "Germany FR", 'Winner'] = "Germany"

    # Make sure to return the latest dataframe

    return df3

def load_and_process2(url_or_path_to_csv_file):
    #Prepare for lists needed
    DeleteList=["Datetime","Stage","City","Stadium","Attendance","RoundID",
            "MatchID","Home Team Initials","Away Team Initials","Win conditions",
            "Half-time Home Goals","Half-time Away Goals","Assistant 1","Assistant 2","Referee"]
    df = load_and_process1("../data/raw/WorldCups.csv")
    
    #Method Chain 1 (Load data;
    #Drop unneccessary columns;drop N/A rows; change data type)
    df1=(
        pd.read_csv(url_or_path_to_csv_file)
        .drop(DeleteList, axis=1).dropna().astype({'Year': 'int64'})
    )
    
    #Method Chain 2
    df2=(df1[df1['Year']
         .isin(df['Year'])]
     .reset_index().drop("index", axis=1)
    )
    
     # Make sure to return the latest dataframe
    return df2

def load_and_process2(url_or_path_to_csv_file):
    #Prepare for lists needed
    DeleteList=["Datetime","Stage","City","Stadium","Attendance","RoundID",
            "MatchID","Home Team Initials","Away Team Initials","Win conditions",
            "Half-time Home Goals","Half-time Away Goals","Assistant 1","Assistant 2","Referee"]
    df = load_and_process1("../data/raw/WorldCups.csv")
    
    #Method Chain 1 (Load data;
    #Drop unneccessary columns;drop N/A rows; change data type)
    df1=(
        pd.read_csv(url_or_path_to_csv_file)
        .drop(DeleteList, axis=1).dropna().astype({'Year': 'int64'})
    )
    
    #Method Chain 2 (Filter winning years; reset index)
    df2=(df1[df1['Year'].isin(df['Year'])]
     .reset_index().drop("index", axis=1)
    )
    
        #Make a Home Team dataframe
        #Method Chain 1 (Filter a Home Team List with selected columns)
    df_H1=df2[['Year','Home Team Name','Home Team Goals']].copy()
    
        #Method Chain 2 (Filter rows, reset index)
    df_H2=(
        df_H1[df2['Home Team Name'].isin(df['Winner'])]
        .reset_index().drop("index", axis=1)
    )
    
        #Method Chain3
    df_H3=(
        pd.merge(left=df, right=df_H2, left_on=["Year", "Winner"], right_on=["Year", "Home Team Name"])
        .drop("Winner",axis=1).rename(columns={"Home Team Name":"Team Name","Home Team Goals":"Team Goals"})
    )
    
        #Make a Away Team dataframe
        #Method Chain 1 (Filter a Away Team List with selected columns)
    df_A1=df2[['Year','Away Team Name','Away Team Goals']].copy()
    
        #Method Chain 2 (Filter rows, reset index)
    df_A2=(
        df_A1[df2['Away Team Name'].isin(df['Winner'])]
        .reset_index().drop("index", axis=1)
    )
    
        #Method Chain3
    df_A3=(
        pd.merge(left=df, right=df_A2, left_on=["Year", "Winner"], right_on=["Year", "Away Team Name"])
        .drop("Winner",axis=1).rename(columns={"Away Team Name":"Team Name","Away Team Goals":"Team Goals"})
    )
    
    #Method Chain3 (Merging Away Team and Home Team df, reset index, Drop the "Year" column)
    df3=pd.concat([df_H3, df_A3]).sort_values(by=["Year"]).reset_index().drop(["index"], axis=1)

    return df3