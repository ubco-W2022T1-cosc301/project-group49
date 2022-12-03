# Final Report Group 49

## Introduction
Our group explored a Fifa world cup dataset that included information on all games played until the 2014 tournament. When we began the project, the 2022 World Cup was still 2 months away and as we are about to submit our findings, the World Cup is currently happening! It was rewarding to see the data we analyzed come to life, and having a better understanding of the game backed by data. 

## Exploratory Data Analysis

![Heatmap of Fifa dataset](/images/analysis1_eda1.png)  
This EDA heatmap chart from [Analysis 1](notebooks/analysis1.ipynb), shows a summary of the relationships between the numerical data values in my dataset.

![Histogram of goals scored in a game by home team per year](/images/analysis1_eda2.png)  
This histogram  from [Analysis 1](notebooks/analysis1.ipynb), shows a tally of the number of goals scored in a match by the home team across the years. Of course, 0, 1, and 2 are the most common amount. This is a good chart but has too much information and is hard to interpret.

![Heatmap of wrangled Fifa dataset from analysis 3](/images/analysis3_eda1.png)  
This EDA heatmap chart from [Analysis 3](notebooks/analysis3.ipynb), shows a summary of the relationships between the numerical data values.

![Pair plot of the data from analysis 3](/images/analysis3_eda2.png)  
I have used the pair plot in [Analysis 3](notebooks/analysis3.ipynb) to see if there are any trends in other plots that I have missed.  

  

## Research Question 1: Whether 'home team advantage' is reflected in the dataset and if so, how much does it factor into the outcome of the match (by number of goals)?

![](/images/analysis1_rq1.png)  
This simple histogram shows the winner of the game across the years. From this chart we can confidently state that home team advantage is reflected as home team wins are more than double the away team wins. Note that the 'Other' category refers to the game resulting in a draw or penalties. 

![](/images/analysis1_rq2.png)  
Now, looking at the boxplot for the goals scored by the home team and away team, again we see a clear difference between the two. Home teams average more goals and even have a higher upper quartile. Until now, all the graphs we have looked don't take into consideration the year. Let's look into how the year affects our findings. 

![](/images/analysis1_rq3.png)  
This histogram gives us a good understanding of how home team advantage has affected the games. As you can see, towards the beginning of the tournament, in 1930, almost all games were won by the home team. This trend stays the same until around 1986, where away teams also start winning and the 'Other' category also rises. These two have continued to rise gradually until the end of our dataset, 2014. This tells us that games have been getting more competitive and home team advantage plays less into affect as to who the winner of the game is.  


## Research Question 3: Does crowd attendance affects the number of goals scored in the game in any way (increase with more attendance or vice-versa)?

![](/images/analysis3_RQ1.png)  
This simple bar chart shows the affect of attendance on total goals scored in the year 2014. From this chart we can clearly see that the relationhsip between the two variables starts off as positive but higher the number of attendance, chances are scores goals are less likely scored after a certain threshold.

![](/images/analysis3_RQ2.png)  
This histogram gives us a good understanding of the trends of goals scored according to attendance in the year 2014. As you can see, with higher attendance numbers, the average number of goals scored is 3, but with lower crowd attendance, upto 7 goals have been scored.  


## Conclusion

### Analysis 1
In conclusion, Home team advantage has been reflected in the dataset but is more prominent earlier on, between 1930 and 1978. Since then, wins for the away team and the number of tied games have been increasing. This means the games are getting more competitive and players are getting used to the pressure of playing at the opposing team's home pitch. This is good for both, the sport and the viewers!

### Analysis 3
In conclusion, we see that attendance and number of goals scored have a varied relationship throughout the years. In the earlier years, this relationship is seen to be almost proportional but in the more recent seasons most goals are scored when there isn't too much or too little attendance. But by 2014 you clearly see that a larger attendance brings down the number of goals scored which is interesting as one would imagine higher attendance having the opposite effect. From this we can conclude that, higher the number of attendance, chances are scores goals are less likely scored, which is a surprising outcome considering the fact that we would have expected the vice versa because of morale boosts. Soccer/football (whatever you call it in your country) is truly a game of concentration!
