import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import seaborn as sns
from scipy import stats

def create_position_group_df(lst, position_group):
  """Creates a pandas dataframe of combined and aggregated information from multiple datasets.
  the final dataset will have the following information:
  gameId: the unique identifier of the games
  playId: An identifier of the play within a specific gameId
  nflID: A unique identifier of a player
  displayName: The name of the player associated with the nflID
  s: Average speed per play of a player in yards/second
  a: Average acceleration per play of a player in yards/second**2

  Args:
      lst (list): A list of the CSV names to concatenate
      position_group (string): A string representing the type of position within the position column in each weeks csv

  Returns:
      pd.DataFrame: Returns a concatenated dataframe of player metrics in that position group.json
  """
  week_empty = pd.DataFrame({
                            'gameId': [],
                            'playId': [],
                            'nflId': [],
                            'displayName': [],
                            's': [],
                            'a': []
                          })
  for week in lst:
      week = week[week['position'] == position_group][['s','a','nflId', 'displayName', 'playId','gameId']]\
                  .groupby(['gameId','playId', 'nflId', 'displayName']).mean()\
                  .reset_index(level = ['gameId', 'playId', 'nflId', 'displayName'])
      week_empty = pd.concat([week_empty,week], join= 'inner')
  return week_empty