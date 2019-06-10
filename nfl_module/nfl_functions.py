# import for random team name 
from random import choice

# import for getting the website and webscraping data
import requests
from bs4 import BeautifulSoup

# array of all the current NFL teams
nfl_teams_constant = ["Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", 
"Buffalo Bills", "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
 "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans",
"Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs", "Los Angeles Chargers", 
"Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings", "New England Patriots", 
"New Orleans Saints", "New York Giants", "New York Jets", "Oakland Raiders", 
"Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", 
"Tampa Bay Buccaneers", "Tennessee Titans", "Washington Redskins"]

# array of the valid stats to check
valid_stats = ["wins", "losses", "points for", "points against"]

# array of the nfl teams as they appear on the ESPN website
nfl_teams = []

# variables for working with BeautifulSoup
nfl_website = ""
source = ""
nfl_soup = ""


def get_website():
        
    """Gets the ESPN website
    
    Returns
    -------
    web_bool : boolean
        The result of whether the website was obtained successfully. 
    """

    global nfl_website
    global source
    global nfl_soup
    web_bool = True

    try:

        requests.get("http://www.espn.com/nfl/standings")  
    
    # error if the request to get the ESPN NFL standings fails
    except requests.exceptions.RequestException:

        print("Unable to obtain ESPN website.")
        web_bool = False

    # set variables in order to webscrape with BeautifulSoup
    if(web_bool != False):

        nfl_website = requests.get("http://www.espn.com/nfl/standings")
        source = nfl_website.content
        nfl_soup = BeautifulSoup(source, 'html.parser')

    return web_bool


def create_ordered_teams():
    
    """Get array of ordered teams as they appear on the ESPN website"""
    
    # get class that has all the team names
    soup_teams = nfl_soup.find_all(class_="hide-mobile")
    
    for index in soup_teams:
        
        # get the specific team name
        name = index.find('a').text

        # create a NflTeam object for every team and append to nfl_teams
        team = NflTeam(name)
        nfl_teams.append(team)
        

def fill_stats():

    """Fills the wins, losses, points_for, points_against attributes for each NFLTeam object"""

    # gets all of the AFC team table data
    afc_data = nfl_soup.find_all(class_="Table2__tbody")[1].find_all("tr")

    # afc_data index
    x = 0
    # nfl_teams index
    y = 0

    while x < len(afc_data):

        # set the wins, losses, points_for, points_against attributes for the current AFC NFLTeam
        # indice where % 5 == 0 is not a team, so skip over this indice
        if(x % 5 != 0):

            nfl_teams[y].wins = int(afc_data[x].find_all("td")[0].text, 10)
            nfl_teams[y].losses = int(afc_data[x].find_all("td")[1].text, 10)
            nfl_teams[y].points_for = int(afc_data[x].find_all("td")[8].text, 10)
            nfl_teams[y].points_against = int(afc_data[x].find_all("td")[9].text, 10)

            # update indices
            y += 1
            x += 1

        else:

            x += 1

    # gets all of the nfc team table data
    nfc_data = nfl_soup.find_all(class_="Table2__tbody")[3].find_all("tr")

    # nfc_data index
    x = 0
    # nfl_teams index
    y = 16

    while x < len(nfc_data):

        # set the wins, losses, points_for, points_against attributes for the current NFC NFLTeam
        # indice where % 5 == 0 is not a team, so skip over this indice
        if(x % 5 != 0):

            nfl_teams[y].wins = int(nfc_data[x].find_all("td")[0].text, 10)
            nfl_teams[y].losses = int(nfc_data[x].find_all("td")[1].text, 10)
            nfl_teams[y].points_for = int(nfc_data[x].find_all("td")[8].text, 10)
            nfl_teams[y].points_against = int(nfc_data[x].find_all("td")[9].text, 10)

            #update indices
            y += 1
            x += 1

        else:

            x += 1

def set_stat_rank(input_list):
    
    """Set stat_rank, a list that has the ranks of the teams by the stat provided in input_list

    Parameters
    ----------
    input_list : int list
        A list that's ordered from highest to lowest by a set stat(attribute of a team)
    
    Returns
    -------
    stat_rank : int list
        A list that has the ranks of the teams by the stat provided in input_list 
    """

    # variables for indices and starting ranks
    i = 0
    rank = 1 
    starting_data = input_list[i]

    # empty stat_rank
    stat_rank = []
    
    while(i < len(input_list)):
        
        # change the rank and append the new rank, and set the new starting data for 
        # the new rank
        if(input_list[i] < starting_data):
            
            rank += 1
            stat_rank.append(rank)
            
            starting_data = input_list[i]

        # append the same rank
        else:
            
            stat_rank.append(rank)
        
        i += 1
   
    return stat_rank

    
def team_sort_by_stat(team, stat):

    """Creates a list of NFLTeams sorted by stat, a list of ints of just the sorted stat,
       and a string for input 

    Parameters
    ----------
    team : string
        Team name

    stat : string
        Stat we are giving information for
    
    Returns
    -------
    [new_list, stat_list, future_string] : [NFLTeam list, int list, string]
        The two set lists and the string as a list      
    """
    
    # empty stat_list and future_string 
    stat_list = []
    future_string = ""
    
    # sort the teams basesd on the input stat
    i = 0

    if(stat == "wins"):
        
        # sort teams(highest to lowest) by wins
        new_list = sorted(nfl_teams, reverse = True, key = lambda x: x.wins)
        
        # fill stat_list
        while(i < len(new_list)):
            
            # set future string
            if(new_list[i].team_name == team):
            
                future_string = "- Total wins: " + str(new_list[i].wins)

            stat_list.append(new_list[i].wins)
            
            i += 1
    
    elif(stat == "losses"):
        
        # sort teams(highest to lowest) by losses
        new_list = sorted(nfl_teams, reverse = True, key = lambda x: x.losses)
        
        # fill stat_list
        while(i < len(new_list)):
            
            # set future string
            if(new_list[i].team_name == team):
                
                future_string = "- Total losses: " + str(new_list[i].losses)

            stat_list.append(new_list[i].losses)
            
            i += 1
    
    elif(stat == "points for"):
        
        # sort teams(highest to lowest) by points_for
        new_list = sorted(nfl_teams, reverse = True, key = lambda x: x.points_for)
        
        # fill stat_list
        while(i < len(new_list)):
            
            # set future string
            if(new_list[i].team_name == team):
                
                future_string = "- Total points for: " + str(new_list[i].points_for)

            stat_list.append(new_list[i].points_for)
            
            i += 1 
    
    elif(stat == "points against"):
    
        # sort teams(highest to lowest) by points_against
        new_list = sorted(nfl_teams, reverse = True, key = lambda x: x.points_against)
        
        #fill stat_list 
        while(i < len(new_list)):
        
            # set future string
            if(new_list[i].team_name == team):
                
                future_string = "- Total points against: " + str(new_list[i].points_against)

            stat_list.append(new_list[i].points_against)
            
            i += 1

    return [new_list, stat_list, future_string]


def tied_create(index, input_list_stat, input_list_name):
    
    """Set tied_list, a list of all the teams that are tied in the input stat with the input team

    Parameters
    ----------
    index : int
        Index of team we are comparing against

    input_list_stat : int list
        A list containing just the sorted stats
    
    input_list_name : NFLTeam list
        A list containing the sorted NFLTeams objects
    
    Returns
    -------
    tied_list : NFLTeam list
        A list of all the NFLTeam objects that have the same input_list_stat 
    """
    
    x = 0
    tied_list = []
    
    while(x < 32):
    
        # don't include index, which would be tied with itself
        if(x != index):
    
            if(input_list_stat[x] == input_list_stat[index]):
    
                tied_list.append(input_list_name[x])
    
        x += 1
    
    return tied_list


def sort_by_stat(team, stat):

    """Prints the stats for the specified team

    Parameters
    ----------
    team : string
        Team name

    stat : string
        Stat we are giving information for
    """
    
    # get rid of whitespace before and after stat
    stat = stat.strip()
    
    # sort the teams basesd on the input stat
    ordered_list_fullTeam = team_sort_by_stat(team, stat)
    
    # team name, sorted by input stat
    ordered_list_name = ordered_list_fullTeam[0]
    
    # just sorted by stat
    ordered_list_stat = ordered_list_fullTeam[1] 

    # set future_string
    future_string = ordered_list_fullTeam[2]

    # set stat_rank
    stat_rank = set_stat_rank(ordered_list_stat)
                 
    # get index of input team
    index = 0
    x = 0
    
    while(x < len(ordered_list_name)):
    
        # stopping index if true
        if(ordered_list_name[x].team_name == team):

            index = x
            break
    
        x += 1

    # get all the teams that are tied in the input stat with the input team
    tied_list = tied_create(index, ordered_list_stat, ordered_list_name)
    
    # printed out response to the user 
    print("\n*Rank is determined without tiebreakers. Ranks for " + stat + " go from 1-" + 
        str(stat_rank[-1]) + ".")
    print(future_string)
    print("- Rank: " + str(stat_rank[index]))
    
    # if tied_list is empty
    if(len(tied_list) != 0):
       
        # create string of tied teams
        tied_teams = ""
        
        for value in tied_list:
        
            tied_teams +="  " +  value.team_name + "\n"
        
        print("- Tied for rank " + str(stat_rank[index]) + " in " + stat + " with the:\n" + 
             tied_teams)


def random_team():

    """get and return random nfl team
    
    Returns
    -------
    choice(nfl_teams_constant)
        A string from nfl_teams_constant
    """

    return choice(nfl_teams_constant)


def check_team(input_team):

    """Check if input_team is equal to one of the strings in nfl_teams_constant. Returns True if 
    it is, False if not

    Parameters
    ----------
    input_team : string
        A string
    
    Returns
    -------
    boolean
        True or False 
    """

    # get rid of whitespace before and after input_team
    input_team = input_team.strip()

    if input_team in nfl_teams_constant:
        
        return True

    return False


def check_stat(input_stat):

    """Check if input_stat is equal to one of the strings in valid_stats. Returns True if 
    it is, False if not

    Parameters
    ----------
    input_stat : string
        A string
    
    Returns
    -------
    boolean
        True or False 
    """

    # get rid of whitespace before and after input_stat
    input_stat = input_stat.strip()
    
    if input_stat in valid_stats:
        
        return True
    
    return False


def exit_check(input_string):
    
    """Check if input_string is equal to 'exit'. Returns True if it is, False if not

    Parameters
    ----------
    input_string : string
        A string
    
    Returns
    -------
    boolean
        True or False 
    """

    # get rid of whitespace before and after input_string
    input_string = input_string.strip()

    if(input_string == "exit"):
        
        return True

    return False


class NflTeam():

    """Object representing an NflTeam with class attributes for amount of wins, losses,
     points for and points against, and an instance attribute for team name
    """
   
    # attributes set to None
    wins = None
    losses = None
    points_for = None
    points_against = None

    def __init__(self, name):
        
        # set team_name instance attribute
        self.team_name = name

    
