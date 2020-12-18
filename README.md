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
In recent years NFL offenses have become faster and have been scoring more points. There is some speculation that the increased points are in part due to NFL rule changes that benefit the passing game. In the past, sending a wide receiver across the middle of the field would innevitably result in that player ending up on the ground whether they were the recipient of the pass or not. Defenses could run buckshot from sideline to sideline and most collisions were seen as part of the game. That is no longer the case. There are now extensive rules about who can get hit and how and where you can hit them. There are also some strict rules about how a pass can be defensed. If a defender doesn't do everything right fans of the game will see a yellow penalty flag on the field and most likely result in Pass Interference. Pass interference is inforced at the spot of the foul, which often results in 30 yards or more in penalty yardage and makes it the most costly penalty in the game.  For these reasons and more teams seem to be focusing less on winning at the line of scrimmage with size and strength and instead they are getting off the line of scrimmage with speed and are throwing the ball more often. That brings us to my main question going into this project. Can the average speed per play of NFL Cornerbacks defending these fast wide receivers be a predictor for their success on passing plays? With that in mind I came up with this hypothesis test:

##### Null Hypothesis : The top 25% fastest CB's will have no difference in average EPA. 
##### Alternative Hypothesis: The top 25% fastest CB's will have a lower average EPA. 


### The Data
To answer this question I found a dataset on Kaggle of data from 2017. It consisted of four types of CSV files.

Here is the link to the original dataset: [NFL Big Data Bowl](https://www.kaggle.com/c/nfl-big-data-bowl-2021/notebooks)

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

### What the Data is Telling Me

As mentioned above I am working with the following Null and alternate hypothesis test.

##### Null Hypothesis : The top 25% fastest CB's will have no difference in average EPA
##### Alternative Hypothesis: The top 25% fastest CB's will have a lower average EPA. 

I tested the top 25% of Cornerbacks by average speed per play in yards/second against the bottom 25% of corner backs in that same space. I used a MannwhitneyU test and got a P-value of 0.8346076309665449. Given that my alpha for this test was .05, I definitely do not have enough evidence to reject my null hypothesis.

Looking at these two distibutions we can see that this p_value result makes sense.

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Distribution%20of%20Average%20EPA:%20Cornerbacks.png)

Frankly I was a bit surprised to see this result, so I started to investigate a little deeper. 

If we look at a plot of all the Average speeds vs. all of the the Average EPA per play you can see that this is very spread out. 

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Corner%20Back%20Average%20Speed%20Vs.%20Average%20EPA.png)

We can also see here that the top ranked Cornerbacks by Pro Football Focus from the 2017 season vary in where they land on either side of the mean of Average speed per play. Some of them are quite a bit slower than their peer by that metric. 

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Top%20CB%20Against%20the%20Average%20Speed.png)

Source for Top Ten list: [Pro Football Focus: NFL Top 15 Cornerbacks](https://www.pff.com/news/pro-hayward-ramsey-headline-the-nfls-top-cornerbacks-heading-into-2018)

So this also ultimately supports our final conclusion that we cannot reject the null. So what is possibly going on here?

### Putting our Data into Context

I have found through analysis of this data that Average speed per play is not an appropriate metric for determining a cornerbacks success against the pass. There are a couple of things that we can look at here that might explain why. 

---

Cornerbacks are often at their fastest when they are trying to make up for a bad play. 

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Corner%20back%20is%20beat.gif)

- You can see in the video above that the Cornerback is beat around the edge and then has to put in a great effort of speed and accelerattion to catch up. Every cornerback will get beat every once in a while, but the bad cornerbacks who get beat often will have to make up for this with the speed to catch up to their opponent.

---

There are many occasions where the Cornerback will be playing off the defender or in zone defense and average speed on that play is going to be much less of a factor. In these situation peak speed and/or peak acceleration may be a good metric, but average speed much less so. The reason is that the defender waits inside of a zone for a skill player who is attacking that part of the field. The act of moving in this situation happens much more quickly as opposed to following a receiver of the line and tracking their steps throughout. 

Zone coverage:

![alt link](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Zone%20Defense.gif)

Man Coverage:
![alt link](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Man%20coverage.gif)




