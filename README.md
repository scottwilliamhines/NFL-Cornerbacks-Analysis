# NFL-Cornerbacks-Analysis
NFL Cornerback: What Statistics Have an Effect on EPA


### A Brief Explanation of Terms

**Cornerback**
A Cornerbacks main role on an NFL defense is to protect against plays going to the pass catchers on the offense. Though it is not a hard and fast rule, this usually means that they are tracking the wide receivers. We know that in 2017 the NFL offenses operated with 1 Running Back, 1 Tight End, and 3 Wide Receivers 71.29% of the time. The ball can be passed to any of these positions, but most often it is going to the Wide Receivers. So the cornerbacks job is to track that wide receiver well enough to be able to keep the ball out of their hands if the pass comes their way. 

![alt text](https://github.com/scottwilliamhines/NFL-Cornerbacks-Analysis/blob/main/img/Cornerback%20example.gif)

**EPA (Expected Points Added)**
Expected points added on the play, relative to the offensive team. Expected points is a metric that estimates the average of every next scoring outcome given the play's down, distance, yardline, and time remaining (numeric). Within this dataset what we are seeing is a change in EPA on each particular play. Offenses want a higher number here because it shows that they made progress towards a higher probability of scoring points. Defenses and defensive players on the otherhand will want this number to be low or negative as that indicates they successfully limited the increase in probability of points or even decreased that probability. I will be averaging this metric out per Cornerback and per play, so in our final dataset the numbers we are seeing represent an Average change in EPA per passing play that each cornerback acheived on the 2017 season. 

### Can speed predict success of NFL Cornerbacks against the pass?
In recent years NFL offenses have become faster and have been scoring more points. There is some speculation that the increased points are in part due to NFL rule changes that benefit the passing game. In the past, sending a wide receiver across the middle of the field would innevitably result in that player ending up on the ground whether they were the recipient of the pass or not. Defenses could run buckshot from sideline to sideline and most collisions were seen as part of the game. That is no longer the case. There are extensive rules about who can get hit and how and where you can hit them now. There are also some strict rules about how a pass can be defensed. If a defender doesn't do everything right the fan will see a yellow penalty flag on the field and most likely result in Pass Interference. Pass interference is inforced at the spot of the foul, which often results in 30 yards or more in penalty yardage and makes it the most costly penalty in the game.  Because of this teams seem to be focusing less on winning at the line of scrimmage with size and strength and instead they are getting off the line of scrimmage with speed and are throwing the ball more often. That brings us to my main question going into this project. Can the average speed of NFL Cornerbacks defending these fast wide receivers be a predictor for their success on passing plays?

