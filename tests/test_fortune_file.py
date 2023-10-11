"""Test fortune_file classes"""
# flake8: noqa
from vaticinator.fortune_file import (
    FortuneFile, FortuneDirectory,
    FortuneCollection, DEFAULT_FORTUNE_PATH
    )

def test_fc():
    """Test FortuneCollection."""
    coll = FortuneCollection()
    coll.add_path(DEFAULT_FORTUNE_PATH)
    f = coll.get_random_file()
    ff = coll.get_random_fortune()
    assert True


def test_fd():
    """Just asserts True."""
    fdir = FortuneDirectory(DEFAULT_FORTUNE_PATH)
    assert len(fdir.filenames) > 0
