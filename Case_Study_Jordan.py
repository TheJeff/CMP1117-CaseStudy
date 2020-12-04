# ----------------------------------------------------------------------
# Title:Homework 10
# Jordan Cerilli, A00132189
# Date:2020,11,04
# Purpose:Identify Class Car
# Acknowledgments:N/A
# -----------------------------------------------------------------------
import pickle

def main():

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
            add1 = input('Players Name: ')
            add2 = input('Players Age: ')
            add3 = input('Players Games Played: ')
            add4 = input('Players Games They Have Started In: ')
            add5 = input('Players Minutes Played This Season: ')
            add6 = input('Players Feild Goals Made This Season: ')
            add7 = input('Players Feild Goal Attempts This Season: ')
            add8 = input('Players Feild Goal Percentage: ')
            add9 = input('Players 3-Pointers Made: ')
            add10 = input('Players 3-Pointers Attempted: ')
            add11 = input('Players 3-Pointer Percentage: ')
            add12 = input('Players 2-Pointers Made: ')
            add13 = input('Players Free Throws Made: ')
            add14 = input('Players Free Throw Attempts: ')
            add15 = input('Players Free Throw Percentage: ')
            add16 = input('Players Offesive-Rebounds This Season: ')
            add17 = input('Players Defensive-Rebounds This Season: ')
            add18 = input('Players Total-Rebounds This Season: ')
            add19 = input('Players Total Assists This Season: ')
            add20 = input('Players Total Steals This Season: ')
            add21 = input('Players Total Blocks This Season: ')
            add22 = input('Players Total Turnovers This Season: ')
            add23 = input('Players Total Personal Fouls This Season: ')
            add24 = input('Players Total Points: ')

        if menu_choice == '2':
            # Delete            
        if menu_choice == '3':
            print(infile)
        if menu_choice == '4':
            with open("team.dat", "wb") as infile:
                pickle.dump(team, infile)
        elif menu_choice == 'Q' or menu_choice == 'q':
            print(' Goodbye')
        else:
            print(' Not a valid choice, try again.')
            pickle.dump(person, file)
# Call the main function and start the program.
main()
