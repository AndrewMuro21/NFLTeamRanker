# get funtions in order to answer the prompts
import nfl_module.nfl_functions as nfl#.nfl_functions as nfl

# only run program if site was successfully obtained
if(nfl.get_website() == True):
    
    # create team objects for every team and set their stats according to their appearnce on
    # the website
    nfl.create_ordered_teams()
    nfl.fill_stats()

    # introduction
    print("Welcome to Team Ranker-NFL Edition(2018), where you can see where NFL teams stack up"
         " against their competitors. To use Team Ranker-NFL Edition(2018), simply follow the" 
         " prompts by entering the correct information. If at any point you would like to leave,"
         " input 'exit' and then press enter. Enjoy.\n\n")

    # set initial prompt value
    prompt = 1

    # keep running prompt until prompt == terminate
    while(True):

        # exit program
        if(prompt == "terminate"):
        
            print("\nThank you for using Team Ranker-NFL Edition(2018).")
            break
        
        # try and get team name from the user input
        elif prompt == 1:
            
            # ask for team name and get input
            print("Please enter a valid team name(include city and organization name, e.g., "
                 + nfl.random_team() + "):")
            team = input()

            # exit check
            if(nfl.exit_check(team) == True):
                
                prompt = "terminate"

            # team check
            if(prompt != "terminate"):
                
                if(nfl.check_team(team) == True):
                
                    prompt = 2
                    print("\n")

        # try and get input stat for the selected team
        elif prompt == 2: 
            
            # ask which stat they would like to check and get input
            print("Which stat would you like to check for the " + team + "?" + "\nPlease input" 
                 "one of the following.\n(wins -- losses -- points for -- points against)")
            stat = input()

            # exit check
            if(nfl.exit_check(stat) == True):
               
                prompt = "terminate" 

            if(prompt != "terminate"):
                
                # check if valid stat
                if(nfl.check_stat(stat) == True):
                    
                    # run the appropriate stat method
                    nfl.sort_by_stat(team, stat)

                    # keep running prompt of checking stats until the user wants to stop 
                    while(True):
                        
                        # ask for another stat and get input
                        print("\nWould you like to check another stat for the " + team + 
                             "? Input 'yes' or 'no'.")
                        response = input()
                        
                        # exit check
                        if(nfl.exit_check(response) == True):
                        
                            prompt = "terminate" 
                            break
                        
                        # set prompt to different team prompt
                        elif(response == "no"):
                        
                            prompt = 3
                            break
                        
                        # stay in prompt 2
                        elif(response == "yes"):
                        
                            print("\n")
                            break
                        
                        # invalid input
                        else:
                        
                            print("\nInvalid input. Please try again.\n")

                # invalid input               
                else:

                    print("\nInvalid stat. Please try again\n") 

        # try and see if user wants to check stats for a different team
        elif prompt == 3:

            # ask for different team and get input
            print("\nWould you like to check stats for a different team? Input 'yes' or"
                 " 'no'.")
            team_response = input()
            
            # exit check
            if(nfl.exit_check(team_response) == True):
            
                prompt = "terminate" 
            
            # exit check for done with checking stats
            elif(team_response == "no"):
            
                prompt = "terminate"
            
            # set prompt to asking for team name
            elif(team_response == "yes"):
            
                prompt = 1
                print("\n")
            
            # invalid input
            else:
            
                print("\nInvalid input. Please try again\n")
