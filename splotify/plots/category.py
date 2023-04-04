# TODO: call Data.get_data() during __init__.
import plotly.express as px


class CategoryPlot:
    """Object to plot the categories of a group of tracks.

    Supports bar charts and pie charts. Good for looking at the composition of
    playlists (i.e. how many songs are from each album/artist).

    """

    def __init__(self, tracks):
        """Initializes an `CategoryPlot` object to plot the categories of a
        group of tracks.

        Args:
            tracks (pd.DataFrame): A Pandas Dataframe, preferably obtained by
                from calling Data.get_data()

        """
        self.df = tracks

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
