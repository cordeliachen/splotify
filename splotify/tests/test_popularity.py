from splotify.plots import popularity
from splotify.tests import sp
from splotify.data import Data
import unittest.mock as mock
import pytest
import os


@pytest.fixture(scope="module")
def vcr_cassette_dir(request):
    return os.path.join("splotify/tests/cassettes", request.module.__name__)


@pytest.fixture
def pp(track_data):
    with mock.patch("splotify.data.Data.get_data") as get_data:
        get_data.return_value = track_data
        yield popularity.PopularityPlot(sp, Data(sp))


@pytest.mark.vcr()
def test_track_bar_chart(pp):
    fig = pp.track_bar_chart()

    assert fig is not None


@pytest.mark.vcr()
def test_album_bar_chart(pp):
    fig = pp.album_bar_chart()

    assert fig is not None
