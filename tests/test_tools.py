from xatch.tools import slicer


def test_slicer():
    assert slicer[1:10:2] == slice(1, 10, 2)
