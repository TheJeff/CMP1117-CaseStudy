import pickle
import player_builder as pb

def main():
# File 1
    with open("Glossary.txt", "r") as infile:
        glossary = infile.read().splitlines()
    
# File 2
    team = {}
    players = 0

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
    index = 0
    while index < players:
        team[index].printStats(1)
        index +=1 
# Main Menu
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

        elif menu_choice == '2':
            # Get user to enter player name to remove
            # call deletePlayer
            pass 
                     
        elif menu_choice == '3':
            # print top_bar and
            # teamAverage

            pass

        elif menu_choice == '4':

            with open("team.dat", "wb") as infile:
                pickle.dump(team, infile)
            
            print('Team has been pickled as team.dat')
        
        elif menu_choice == '5':
            print('Exported to output.txt')
            exportTeam(team)
        
        elif menu_choice == 'Q' or menu_choice == 'q':
            print(' Goodbye')
        else:
            print(' Not a valid choice, try again.')


    #TODO Team Average Function

    #TODO Print Team List

    #TODO Export Team List



def getTeamAverage(local_team):
    # declare 10 lists one for each stat and for the team averages
    # to return
    # while loop with index to iterate through entire dict
    # add each stat to its corresponding list
    # calculate average and add to team averages list


    #TODO

    #return average list
    pass


def deletePlayer(player_name):
    # iterate through player dictionary
    # pop the entry and rebuild dictionary
    # make players = len(the dictionary)

    pass

def printTeam(local_team):
    # While loop with index
    # each loop call players[index].toString(0)
    # format it, print it. 

    #TODO

    pass

def exportTeam(local_team):
    # Similar to print method but adding to a file 
    # with a space between the stats, team average, 
    # and Glossary

    pass


main()