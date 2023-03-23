import plotly.express as px

# Generate plots to view the makeup of playlists


class CategoryPlot:
    def __init__(self, tracks):
        self.df = tracks

    def bar_chart(self, type="album"):
        grouped_df = self.df[type].value_counts()
        grouped_df = grouped_df.reset_index()
        grouped_df.columns = [type, "count"]
        fig = px.bar(grouped_df, x=type, y="count")
        fig.show()
        return fig

    def pie_chart(self, type="album"):
        grouped_df = self.df[type].value_counts()
        grouped_df = grouped_df.reset_index()
        grouped_df.columns = [type, "count"]
        fig = px.pie(grouped_df, values="count", names=type)
        fig.show()
        return fig
