# TODO: call Data.get_data() during __init__.

"""`CategoryPlot` class.

This module contains the `CategoryPlot` class that plots the categories of your
selected tracks.

"""

import plotly.express as px


class CategoryPlot:
    """Object to plot the categories of a group of tracks.

    Supports bar charts and pie charts. Good for looking at the composition of
    playlists (i.e. how many songs are from each album/artist).

    Args:
        data (splotify.data.Data): A `Data` instance.

    """

    def __init__(self, data):
        self.df = data.get_data()

    def bar_chart(self, groupby="album"):
        """Plots the grouped tracks in a bar chart.

        Groups the tracks based on the `groupby` parameter, counts the
        number of tracks of each group, and plots the counts.

        Args:
            groupby (:obj:`str`): What to group the tracks by. Currently only
                supports 'artist' and 'album'. Defaults to 'album'.

        """
        grouped_df = self.df[groupby].value_counts()
        grouped_df = grouped_df.reset_index()
        grouped_df.columns = [groupby, "count"]
        fig = px.bar(grouped_df, x=groupby, y="count", color=groupby)
        fig.show()
        return fig

    def pie_chart(self, groupby="album"):
        """Plots the grouped tracks in a pie chart.

        Groups the tracks based on the `groupby` parameter, counts the
        number of tracks of each group, and plots the counts.

        Args:
            groupby (:obj:`str`): What to group the tracks by. Currently only
                supports 'artist' and 'album'. Defaults to 'album'.

        """
        grouped_df = self.df[groupby].value_counts()
        grouped_df = grouped_df.reset_index()
        grouped_df.columns = [groupby, "count"]
        fig = px.pie(grouped_df, values="count", names=groupby)
        fig.show()
        return fig
