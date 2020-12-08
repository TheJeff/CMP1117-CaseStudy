import pickle
import player_builder as pb 

def main():
# File 1
    with open("Glossary.txt", "r") as infile:
        glossary = infile.read().splitlines()
    
# File 2
    team = {}
    player = 0

    with open("Raptors_stats.txt", "r") as infile:
        _unsorted = infile.read().splitlines()
        _unsorted.pop(0)
        for line in _unsorted:
            temp = line.split("\t")
            team[player] = pb(
                temp[0],
                temp[1],
                temp[2],
                temp[3],
                temp[4],
                temp[5],
                temp[6],
                temp[7],
                temp[8]
            )
            player += 1

            


        

    menu_choice = '0'
    while menu_choice != 'Q' and menu_choice != 'q':
        print('Baseketball Players')
        print(' ======================')
        print(' 1) Add')
        print(' 2) Delete')
        print(' 3) Print')
        print(' 4) Save')
        print(' Q) Quit')
        print(' ======================')
        menu_choice = input(' 1.Add 2.Delete 3.Print 4.Save Q.Quit:')
        if menu_choice == '1':

            add_name = input('Players Name: ')
            add_games = int(input('Players Games Played: '))
            add_FG = input('Players Feild Goals Made This Season: ')
            add_3P = input('Players 3-Pointers Made: ')
            add_2P = input('Players 2-Pointers Made: ')
            add_FTP = input('Players Free Throw Percentage: ')
            add_TRB = input('Players Total-Rebounds This Season: ')
            add_AST = input('Players Total Assists This Season: ')
            add_PPG = input('Players Total Points: ')
            team[player] = pb(
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
            pass 
                     
        elif menu_choice == '3':

            pass

        elif menu_choice == '4':

            with open("team.dat", "wb") as infile:
                pickle.dump(team, infile)
        
        elif menu_choice == 'Q' or menu_choice == 'q':
            print(' Goodbye')
        else:
            print(' Not a valid choice, try again.')


    #TODO Team Average Function

    #TODO Print Team List

    #TODO Print Rank Team members



def getTeamAverage(team):
    # For loop through collect stats in 9 variables
    #   

    #TODO

    #return average
    pass

def printTeam(team):
    # For loop through a dictionary and call the player.printStats()

    #TODO

    pass

def exportTeam(team):

    #TODO export team to txt file formatted

    pass

