# NFL-Cornerbacks-Analysis
NFL Cornerback: What Statistics Have an Effect on EPA


### A Brief Explanation of Terms

**Cornerback**
A Cornerbacks main role on an NFL defense is to protect against plays going to the pass catchers on the offense. Though it is not a hard and fast rule, this usually means that they are tracking the wide receivers. We know that in 2017 the NFL offenses operated with 1 Running Back, 1 Tight End, and 3 Wide Receivers 71.29% of the time. The ball can be passed to any of these positions, but most often it is going to the Wide Receivers. So the cornerbacks job is to track that wide receiver well enough to be able to keep the ball out of their hands if the pass comes their way. 

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Cornerback%20example.gif)
- Image source: [Pro Football Focus](https://www.pff.com/news/nfl-highest-graded-man-coverage-cornerbacks-in-2019-marcus-peters-and-marlon-humphrey-baltimore-ravens)


**EPA (Expected Points Added)**
Expected points added on the play, relative to the offensive team. Expected points is a metric that estimates the average of every next scoring outcome given the play's down, distance, yardline, and time remaining (numeric). Within this dataset what we are seeing is a change in EPA on each particular play. Offenses want a higher number here because it shows that they made progress towards a higher probability of scoring points. Defenses and defensive players on the otherhand will want this number to be low or negative as that indicates they successfully limited the increase in probability of points or even decreased that probability. I will be averaging this metric out per Cornerback and per play, so in our final dataset the numbers we are seeing represent an Average change in EPA per passing play that each cornerback acheived on the 2017 season. 

### Can speed predict success of NFL Cornerbacks against the pass?
In recent years NFL offenses have become faster and have been scoring more points. There is some speculation that the increased points are in part due to NFL rule changes that benefit the passing game. In the past, sending a wide receiver across the middle of the field would innevitably result in that player ending up on the ground whether they were the recipient of the pass or not. Defenses could run buckshot from sideline to sideline and most collisions were seen as part of the game. That is no longer the case. There are extensive rules about who can get hit and how and where you can hit them now. There are also some strict rules about how a pass can be defensed. If a defender doesn't do everything right fans of the game will see a yellow penalty flag on the field and most likely result in Pass Interference. Pass interference is inforced at the spot of the foul, which often results in 30 yards or more in penalty yardage and makes it the most costly penalty in the game.  For these reasons and more teams seem to be focusing less on winning at the line of scrimmage with size and strength and instead they are getting off the line of scrimmage with speed and are throwing the ball more often. That brings us to my main question going into this project. Can the average speed of NFL Cornerbacks defending these fast wide receivers be a predictor for their success on passing plays?

### The Data
To answer this question I found a dataset on Kaggle of data from 2017. It consisted of four types of CSV files.

- A file on game data.
- A file on player data
- A file on play data
- 17 individual files with tracking data from each game of each week. These were identically formatted.

For more information about each dataset please see the column descriptions here: [Data Descriptions](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/notebooks/Data%20Descriptions.ipynb)

### The Method

In order to answer my question I had to aggregate the information in all of these datasets down to my target metrics. Within the game, play and weekly tracking data there were unique gameId identifiers for each game. Within the tracking data and the play data each gameId had multiple unique playId's. Finally within the tracking data for each player per week there were frameId which split the players position, speed, acceleration, etc. into 59 frames per play. I took the mean per play of the speed and acceleration columns across all 17 weeks and combined that with the players vital information from the players dataset.

Next I had to combine EPA and playResult data and link it to all of the playId's. I wanted my final dataframe to only include information about passing plays because I am only interested in defending agaist the pass. For that reason, I only pulled EPA data from passing plays. This way when I joined this back on my working dataframe I could remove all rows that had NAN values in EPA. The logic here is that because I only pulled EPA from playId's that were passing plays in the original datset, I could deduce that any other row  with a playId that included NAN in the EPA column was a run play. 

Finally I created a playCount column by summing the number of data points present indexed by GameId and PlayId for each player so that I could identify the number of plays that each player took part in throughout the season. I joined this on the aggregated data mentioned above to create a final dataframe that I could work with.

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/FInal%20Cornerback%20DataFrame%20example.png)



