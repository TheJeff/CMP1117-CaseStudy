# Basketball Statistic Program
#
# Authors:
# Jeffrey N
# Jordan C
# Liam B
# Archie O
#  
# Due Date: 
# December 16th, 2020
#  
# Purpose: 
# CMP 1117 Case Study
#   
# Acknowledgments:
# Python 3 API Library
# Previous Experience with Programming
# Textbook Examples 

import pickle
import player_builder as pb #Jeff

# global variables 
team = {} # Dictionary to hold player objects
players = 0 # No. of Players on the Team


def main():
    global team
    global players


# File 1 Jordan
    with open("Glossary.txt", "r") as infile:
        glossary = infile.read().splitlines()
    

# File 2 Jeff
    with open("Raptors_stats.txt", "r") as infile:
        _unsorted = infile.read().splitlines()
        top_bar = _unsorted[0].split("\t")
        _unsorted.pop(0)
        for line in _unsorted:
            temp = line.split("\t")
            team[players] = pb.Player(
                temp[0],
                float(temp[1]),
                float(temp[2]),
                float(temp[3]),
                float(temp[4]),
                float(temp[5]),
                float(temp[6]),
                float(temp[7]),
                float(temp[8])
            )
            players += 1

 
# Main Menu Jordan
    menu_choice = "0"
    while menu_choice != "Q" and menu_choice != "q":
        print(" Basketball Players")
        print("=======================")
        print(" 1) Add")
        print(" 2) Delete")
        print(" 3) Calculate Team Average")
        print(" 4) Save team to Pickle")
        print(" 5) Load Pickled Team")
        print(" 6) Export team to txt file")
        print(" 7) Print Team")
        print(" 8) Print Specific Player")
        print(" Q) Quit")
        print(" ======================")
        menu_choice = input("Enter Selection: \n")


        if menu_choice == "1":
            # Add Player to Dictionary

            add_name = input("Players Name: ")
            add_games = float(input("Players Games Played: "))
            add_FG = float(input("Players Field Goals Made This Season: "))
            add_3P = float(input("Players 3-Pointers Made: "))
            add_2P = float(input("Players 2-Pointers Made: "))
            add_FTP = float(input("Players Free Throw Percentage: "))
            add_TRB = float(input("Players Total-Rebounds This Season: "))
            add_AST = float(input("Players Total Assists This Season: "))
            add_PPG = float(input("Players Total Points: "))
            team[players] = pb.Player(
                add_name,
                add_games,
                add_FG,
                add_3P,
                add_2P,
                add_FTP,
                add_TRB,
                add_AST,
                add_PPG
            )
            players += 1


        elif menu_choice == "2":
            # Remove player from dictionary

            to_del = input("Which Player to remove?\n")
            deletePlayer(to_del)
                     

        elif menu_choice == "3":
            # print top_bar and
            # teamAverage

            average_list = getTeamAverage(team)

            top_bar_print = (
                "{:<30s} {:<6s} {:<6s} {:<6s} {:<6s}"
                "{:<6s} {:<6s} {:<6s} {:<6s}".format(
                    top_bar[0],
                    top_bar[1],
                    top_bar[2],
                    top_bar[3],
                    top_bar[4],
                    top_bar[5],
                    top_bar[6],
                    top_bar[7],
                    top_bar[8],
                )
            )
            avg_to_print= (
                "{:<30s} {:<6.0f} {:<6.0f} {:<6.0f} {:<6.0f}"
                "{:<6.2f} {:<6.0f} {:<6.0f} {:<6.0f}".format(
                    "Team Averages:",
                    average_list[0],
                    average_list[1],
                    average_list[2],
                    average_list[3],
                    average_list[4],
                    average_list[5],
                    average_list[6],
                    average_list[7],
                )
            )
            print(top_bar_print)
            print("=" * 86)
            print(avg_to_print)


        elif menu_choice == "4":
            # Save pickled file

            with open("team.dat", "wb") as infile:
                pickle.dump(team, infile)
            
            print("Team has been pickled as team.dat")


        elif menu_choice == "5":
            # Load pickled file
            try:
                with open("team.dat", "rb") as existingteam:
                    team = pickle.load(existingteam)
                    print("File found importing to program")
            except EnvironmentError:
                print("No previous team file found")
        

        elif menu_choice == "6":
            # call export method
            print("Exported to output.txt")
            exportTeam(team, top_bar, glossary)


        elif menu_choice == "7":
            # call print method
            printTeam(team, top_bar, glossary)


        elif menu_choice == "8":
            # call printPlayer
            user_input = input("What player would you like to print?\n")
            printPlayer(user_input, top_bar)
        

        elif menu_choice == "Q" or menu_choice == "q":
            print("Goodbye")


        else:
            print("Not a valid choice, try again.")


# Functions

def getTeamAverage(local_team): # Liam
    # declare 9 lists one for each stat and for the team averages
    # to return
    # while loop with index to iterate through entire dict
    # add each stat to its corresponding list
    # calculate average and add to team averages list

    games_list = []
    fg_list = []
    three_p_list = []
    two_p_list = []
    ft_list = []
    trb_list = []
    ast_list = []
    pts_list = []

    averages = []

    for key in local_team:
        temp = local_team[key].toString(1).split("\t")
        games_list.append(float(temp[1]))
        fg_list.append(float(temp[2]))
        three_p_list.append(float(temp[3]))
        two_p_list.append(float(temp[4]))
        ft_list.append(float(temp[5]))
        trb_list.append(float(temp[6]))
        ast_list.append(float(temp[7]))
        pts_list.append(float(temp[8]))
        
    avg_games = sum(games_list) / players
    avg_fg = sum(fg_list) / players
    avg_3p = sum(three_p_list) / players
    avg_2p = sum(two_p_list) / players
    avg_ft = sum(ft_list) / players
    avg_trb = sum(trb_list) / players
    avg_ast = sum(ast_list) / players
    avg_pts = sum(pts_list) / players

    averages.append(avg_games)
    averages.append(avg_fg)
    averages.append(avg_3p)
    averages.append(avg_2p)
    averages.append(avg_ft)
    averages.append(avg_trb)
    averages.append(avg_ast)
    averages.append(avg_pts)


    return averages
    

def deletePlayer(to_remove): # Liam
    # iterate through player dictionary
    # delete player 
    # rebuild dictionary
    # make players = the new length of the dictionary
    global players
    global team

    booleon = True
    key = 0

    while booleon:
        if to_remove in team[key].getName():
             del team[key]
        elif key == len(team): 
            booleon = False
        key += 1

    new_key = 0
    new_dict = {}

    for key in team:
        new_dict[new_key] = team[key]
        new_key += 1
    players = new_key
    team = new_dict


def printTeam(local_team, top, _glossary): # Archie
    # Iterate with for loop
    # each loop call team[index].toString(0)
    # format it, print it. 

    top_bar_list = top

    top_to_print = (
        "{:<30s} {:<6s} {:<6s} {:<6s} {:<6s}"
        "{:<6s} {:<6s} {:<6s} {:<6s}".format(
            top_bar_list[0],
            top_bar_list[1],
            top_bar_list[2],
            top_bar_list[3],
            top_bar_list[4],
            top_bar_list[5],
            top_bar_list[6],
            top_bar_list[7],
            top_bar_list[8]
        )
    )
    print(top_to_print)
    print("=" * 86)

    for key in local_team:
        player_list = local_team[key].toString(1).split("\t")
        player_to_print = (
            "{:<30s} {:<6.0f} {:<6.0f} {:<6.0f} {:<6.0f}"
            "{:<6.2f} {:<6.0f} {:<6.0f} {:<6.0f}".format(
                player_list[0],
                float(player_list[1]),
                float(player_list[2]),
                float(player_list[3]),
                float(player_list[4]),
                float(player_list[5]),
                float(player_list[6]),
                float(player_list[7]),
                float(player_list[8])
            )
        )
        print(player_to_print)
    
    # Print Empty line before averages
    print()

    # Averages
    average_list = getTeamAverage(local_team)
    avg_to_print= (
        "{:<30s} {:<6.0f} {:<6.0f} {:<6.0f} {:<6.0f}"
        "{:<6.2f} {:<6.0f} {:<6.0f} {:<6.0f}".format(
            "Team Averages:",
            average_list[0],
            average_list[1],
            average_list[2],
            average_list[3],
            average_list[4],
            average_list[5],
            average_list[6],
            average_list[7],
        )
    )
    print(avg_to_print)
    
    print()

    # Glossary
    print("Glossary")
    print("="* 86)
    for line in _glossary:
        print(line)
    

def exportTeam(local_team, top, _glossary): # Archie
    # Similar to print method but adding to a file 

    write_list = []
    top_bar_list = top

    top_to_print = (
        "{:<30s} {:<6s} {:<6s} {:<6s} {:<6s}"
        "{:<6s} {:<6s} {:<6s} {:<6s}".format(
            top_bar_list[0],
            top_bar_list[1],
            top_bar_list[2],
            top_bar_list[3],
            top_bar_list[4],
            top_bar_list[5],
            top_bar_list[6],
            top_bar_list[7],
            top_bar_list[8]
        )
    )
    write_list.append(top_to_print)
    write_list.append("=" * 86)

    for key in local_team:
        player_list = local_team[key].toString(1).split("\t")
        player_to_print = (
            "{:<30s} {:<6.0f} {:<6.0f} {:<6.0f} {:<6.0f}"
            "{:<6.2f} {:<6.0f} {:<6.0f} {:<6.0f}".format(
                player_list[0],
                float(player_list[1]),
                float(player_list[2]),
                float(player_list[3]),
                float(player_list[4]),
                float(player_list[5]),
                float(player_list[6]),
                float(player_list[7]),
                float(player_list[8])
            )
        )
        write_list.append(player_to_print)
    
    # Print Empty line before averages
    write_list.append("\n")

    # Averages
    average_list = getTeamAverage(local_team)
    avg_to_print= (
        "{:<30s} {:<6.0f} {:<6.0f} {:<6.0f} {:<6.0f}"
        "{:<6.2f} {:<6.0f} {:<6.0f} {:<6.0f}".format(
            "Team Averages:",
            average_list[0],
            average_list[1],
            average_list[2],
            average_list[3],
            average_list[4],
            average_list[5],
            average_list[6],
            average_list[7],
        )
    )
    write_list.append(avg_to_print)
    
    write_list.append("\n")

    # Glossary
    write_list.append("Glossary")
    write_list.append("="* 86)
    for line in _glossary:
        write_list.append(line)

    # Open file to write to
    with open("output.txt", "w") as outputfile:
        for line in write_list:
            outputfile.write("%s\n" % line)


def printPlayer(player_name, top):
    # Print a specific player
    # Same methodology as printTeam
    # combined with deletePlayer

    top_bar_list = top

    top_to_print = (
        "{:<30s} {:<6s} {:<6s} {:<6s} {:<6s}"
        "{:<6s} {:<6s} {:<6s} {:<6s}".format(
            top_bar_list[0],
            top_bar_list[1],
            top_bar_list[2],
            top_bar_list[3],
            top_bar_list[4],
            top_bar_list[5],
            top_bar_list[6],
            top_bar_list[7],
            top_bar_list[8]
        )
    )

    for key in team:
        if player_name in team[key].getName():
            player_to_format = team[key].toString(1).split("\t")
    try:
        player_to_print = (
            "{:<30s} {:<6.0f} {:<6.0f} {:<6.0f} {:<6.0f}"
            "{:<6.2f} {:<6.0f} {:<6.0f} {:<6.0f}".format(
                player_to_format[0],
                float(player_to_format[1]),
                float(player_to_format[2]),
                float(player_to_format[3]),
                float(player_to_format[4]),
                float(player_to_format[5]),
                float(player_to_format[6]),
                float(player_to_format[7]),
                float(player_to_format[8]),
            )
        )
        print(top_to_print)
        print("=" * 86)
        print(player_to_print)
    except Exception:
        print("Player not found")
        
        
main()