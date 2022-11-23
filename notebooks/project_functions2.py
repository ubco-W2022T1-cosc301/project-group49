#Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as plt

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data)
    df1 = pd.read_csv(url_or_path_to_csv_file)

    # Method Chain 2 (Drop unneccessary columns like the Attendance,
    #Check if the winners are a home team(to make sure that every winner counted is a visiting team);
    
    #Preparing the lists and functions needed
    DeleteList=['Runners-Up','Third','Fourth','QualifiedTeams','MatchesPlayed','Attendance']
    
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