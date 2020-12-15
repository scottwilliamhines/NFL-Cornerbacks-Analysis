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

def create_sns_distplot(data, title, x_label, y_label):
    """Labels an sns.distplot

    Args:
    data (pd.series or lst): [An array of data to plot or an array of pd.series or lists to plot on top of each other]
    title ([string]): [Intended title of the plot]
    x_label ([String]): [Intended label for the X-axis]
    y_label ([String]): [Intended label for the Y-axis]
    """
    ax = sns.distplot(data, kde =True)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    return plt.show()

if __name__ == '__main__':
    data1 = np.random.randint(0 , 100, size = 100)
    data2 = np.random.randint(0 , 100, size = 100)
    create_sns_distplot(data1, 'Test Plot', 'data', 'density')