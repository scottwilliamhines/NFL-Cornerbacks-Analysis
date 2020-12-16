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
    plt.savefig("../img/{}".format('{}.png'.format(title)), dpi = 300)
    return plt.show()

def create_stats_plots(data1, data2, title, x_label, y_label, data1_legend_label, data2_legend_label):
    """Creates overlayed KDE distribution plots of 2 series of data.

    Args:
        data1 (pd.series or list): [An array of data to plot or an array of pd.series or lists to plot on top of each other]
        data2 (pd.series or list): [An array of data to plot or an array of pd.series or lists to plot on top of each other]
        title ([string]): [Intended title of the plot]
        x_label ([String]): [Intended label for the X-axis]
        y_label ([String]): [Intended label for the Y-axis]
        data1_label (String): [In]
    """
    ax = sns.distplot(data1, kde =True, label= data1_legend_label)
    sns.distplot(data2, kde =True, label = data2_legend_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    plt.savefig("../img/{}".format('{}.png'.format(title)), dpi = 300)
    return plt.show()

def create_sns_scatter(df, x_data, y_data, title, x_label, y_label):
    """Create a Seaborn Scatter Plot.

    Args:
        dataset ([pd.DataFrame]): A dataframe containing the dataset
        x_data (pd.Series): One of the columns of the dataframe to plot on the x axis
        y_data (pd.Series): A column of data from the dataframe to plot in relation to the x_data on the y_axis
        title (String): Plot title
        x_label (String): X axis label
        y_label (String): Y axis label
    """
    ax = sns.scatterplot(x = x_data, y = y_data, data = df, hue = x_data, legend =  False)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    plt.savefig("../img/{}".format('{}.png'.format(title)), dpi = 300)
    return plt.show()

if __name__ == '__main__':
    data1 = np.random.randint(0 , 100, size = 100)
    data2 = np.random.randint(0 , 100, size = 100)
    df = pd.DataFrame({'col1': [1,4,2,5,7,4,12,34,23,19,4,5,6,7,5,5,6,8,7],
                        'col2': [3,6,3,6,5,7,5,4,4,3,3,6,7,6,5,5,7,8,7]
    })
    create_sns_distplot(data1, 'Test Plot', 'data', 'density')
    create_stats_plots(data1, data2, 'Test Plot', 'data', 'density', 'data1', 'data2')
    create_sns_scatter(df,'col1','col2', 'Test Plot', 'Column 1', 'Column 2')