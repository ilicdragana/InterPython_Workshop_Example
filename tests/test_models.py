"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected



def test_min_mag_negatives():
   # Test that min_mag function works for negatives
   from lcanalyzer.models import min_mag

   test_input_df = pd.DataFrame(data=[[-7, -7, -3], [-4, -3, -1], [-1, -5, -3]], columns=list("abc"))
   test_input_colname = "b"
   test_output = -7

   assert min_mag(test_input_df, test_input_colname) == test_output


# Parametrization for mean_mag function testing
@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        pytest.approx(3.66,0.01)),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_mean_mag(test_df, test_colname, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from lcanalyzer.models import mean_mag
    assert mean_mag(test_df, test_colname) == expected


def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)
