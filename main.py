import pickle
import player_builder as pb

# global variables 
team = {}
players = 0


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

            
# debugging
 
# Main Menu Jordan
    menu_choice = '0'
    while menu_choice != 'Q' and menu_choice != 'q':
        print('Basketball Players')
        print(' ======================')
        print(' 1) Add')
        print(' 2) Delete')
        print(' 3) Calculate Team Average')
        print(' 4) Save team to pickle')
        print(' 5) Export team to txt file')
        print(' 6) Print Team')
        print(' Q) Quit')
        print(' ======================')
        menu_choice = input('Enter Selection: \n')
        if menu_choice == '1':

            add_name = input('Players Name: ')
            add_games = float(input('Players Games Played: '))
            add_FG = float(input('Players Field Goals Made This Season: '))
            add_3P = float(input('Players 3-Pointers Made: '))
            add_2P = float(input('Players 2-Pointers Made: '))
            add_FTP = float(input('Players Free Throw Percentage: '))
            add_TRB = float(input('Players Total-Rebounds This Season: '))
            add_AST = float(input('Players Total Assists This Season: '))
            add_PPG = float(input('Players Total Points: '))
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

        elif menu_choice == '2':
            to_del = input("Who we kickin?")
            deletePlayer(to_del)
                     
        elif menu_choice == '3':
            # print top_bar and
            # teamAverage
            temp_top_bar = top_bar
            temp_top_bar.pop(0)

            for element in temp_top_bar:
                print(element, end="\t")
            print()
            avg = getTeamAverage(team)

            for element in avg:
                print(round(element, 2), end="\t")
            print()

            

        elif menu_choice == '4':

            with open("team.dat", "wb") as infile:
                pickle.dump(team, infile)
            
            print('Team has been pickled as team.dat')
        
        elif menu_choice == '5':
            #print('Exported to output.txt')
            #exportTeam(team)
            print(team[3].toString(0))

        elif menu_choice == '6':
            # call print method
            index = 0
            topbar = team[0].getStatNames()
            print(topbar)
            while index < players:
                team[index].printStats(1)
                index +=1
        
        elif menu_choice == 'Q' or menu_choice == 'q':
            print('Goodbye')
        else:
            print('Not a valid choice, try again.')


    #TODO Team Average Function (Temporarily done)

    #TODO Delete Player (Temporarily done)

    #TODO Print Team List

    #TODO Export Team List



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
    


def deletePlayer(player_name): # Liam
    # iterate through player dictionary
    # pop the entry and rebuild dictionary
    # make players = the new length of the dictionary
    global players
    global team
    
    to_pop = -1
    for key in team:
        if player_name in team[key].getName():
            to_pop = key
    try:
        team.pop(to_pop)
    except Exception:
        pass

    new_key = 0
    temp_dict = {}
    for key in team:
        temp_dict[new_key] = team[key]
        new_key += 1
    players = new_key
    team = temp_dict



def printTeam(local_team): # Archie
    # While loop with index
    # each loop call players[index].toString(0)
    # format it, print it. 

    #TODO

    pass

def exportTeam(local_team): # Archie
    # Similar to print method but adding to a file 
    # with a space between the stats, team average, 
    # and Glossary

    pass


main()