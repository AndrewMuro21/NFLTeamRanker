# get function from nfl_functions.py
from . import nfl_functions

 
def test_check_team():
    """test check_team functionality"""

    assert nfl_functions.check_team("Los Angeles Chargers") == True


def test_get_website():
   """test successful website retrieval"""

   assert nfl_functions.get_website() == True


def test_stats_for_saints():
    """test successful stats for New Orleans Saints"""

    # create team objects for every team and set their stats according to their appearnce on
    # the website
    nfl_functions.create_ordered_teams()
    nfl_functions.fill_stats()

    for index in nfl_functions.nfl_teams:

        if(index.team_name == "New Orleans Saints"):
            
            assert index.wins == 13
            assert index.losses == 3
            assert index.points_for == 504
            assert index.points_against == 353


# for this test, running pytest calls get_website(), create_ordered_teams(), and fill_stats()
# so we don't need to call them again
def test_set_stat_rank():
    """test stat_rank for wins is correct"""

    assert nfl_functions.set_stat_rank(nfl_functions.team_sort_by_stat("Los Angeles Rams",
    "wins")[1]) == [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8,
     8, 9, 9, 9, 10, 10, 10, 11]
