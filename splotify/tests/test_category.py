from splotify.plots import category
from splotify.data import Data
from splotify.tests import sp
import unittest.mock as mock
import pytest


@pytest.fixture
def cp(track_data):
    with mock.patch("splotify.data.Data.get_data") as get_data:
        get_data.return_value = track_data
        yield category.CategoryPlot(Data(sp))


def test_bar_chart(cp):
    fig = cp.bar_chart("artist")

    assert fig is not None


def test_pie_chart(cp):
    fig = cp.pie_chart("artist")

    assert fig is not None
