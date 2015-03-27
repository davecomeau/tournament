#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *
import math
import os
import random
import time

#number_of_players = 128 
#game_type = "knitting"
#rounds_count = math.log(number_of_players,2)

clear = lambda: os.system('clear')


# Simulate match and record the results
def simulateMatch(player1,player2):
    teams = [player1,player2]
    random.shuffle(teams)
    reportMatch(teams[0],teams[1])
    

# Main
if __name__ == '__main__':
    clear()

    print "\n\t-------------------------------"
    print "\t TOURNAMENT CREATE-A-TRON 3000 "
    print "\t-------------------------------\n\n"

    print "\tLets build a tournament!\n"
    
    print "\tYou have a number of tournament types to choose from:" 
    print "\t\t1. Knitting Tournament"
    print "\t\t2. Cockroach Racing"
    print "\t\t3. Beer Chugging Challenge"
    print "\t\t4. Jousting Match"
    print "\t\t5. Staring Contest"

    while True:
        try:
            choice = int(raw_input("\n\tWhich type of tournament are you creating? "))
        except ValueError:
            print "\tPlease enter a valid choice..."
            continue

        if choice == 1:
            game_type = "Knitting"
            break
        elif choice == 2:
            game_type = "Cockroach Racing"
            break
        elif choice == 3:
            game_type = "Beer Chugging"
            break
        elif choice == 4:
            game_type = "Jousting"
            break
        elif choice == 5:
            game_type = "Staring"
            break
        else:
            print "\tNeed a valid choice!"

    clear()
    print "\n\t-------------------------------"
    print "\t TOURNAMENT CREATE-A-TRON 3000 "
    print "\t-------------------------------\n\n"
    print "\tYou have a choice of tournament sizes:\n" 
    print "\t\t1. 4 Players"
    print "\t\t2. 8 Players"
    print "\t\t3. 16 Players"
    print "\t\t4. 32 Players"
    print "\t\t5. 64 Players"

    while True:
        try:
            choice = int(raw_input("\n\tHow many players in your tournament? "))
        except ValueError:
            print "\tPlease enter a valid choice..."
            continue

        if choice == 1:
            number_of_players = 4
            break
        elif choice == 2:
            number_of_players = 8
            break
        elif choice == 3:
            number_of_players = 16
            break
        elif choice == 4:
            number_of_players = 32
            break
        elif choice == 5:
            number_of_players = 64
            break
        else:
            print "Need a valid choice!"
        

    rounds_count = math.log(number_of_players,2)
    match_count = number_of_players -1

    clear()
    print "\n\t--------------------------------------"
    print "\tWelcome to the " + game_type +" tournament!"
    print "\t--------------------------------------\n\n"
    print "\tWe have " + str(number_of_players) + " players ready to face off over " + str(rounds_count) + " rounds of intense " + game_type + " action!\n\n"
    time.sleep(2)
    print "\t\tRound 1 complete!"
    time.sleep(1)

    # Clear the Players and Matches tables
    deletePlayers()
    deleteMatches()
    
    # register players
    i = 0
    while i < number_of_players: 
        registerPlayer("Player " + str(i + 1))
        i+=1

    # Round 1 - need to randomly assign first match as all participants have 0 wins
    roster = playerStandings()
    i = 0
    
    while i < number_of_players:
        p1_id = roster[i][0]
        p2_id = roster[i+1][0]
        simulateMatch(p1_id,p2_id)
        #print "matching " + roster[i][1]+ " with " + roster[i+1][1]
        i+=2
 
    # Simulate the remaining rounds
    round = 2;

    while round <= rounds_count:
        print "\t\tRound " + str(round) + " complete!"
        roster = swissPairings()
        for team in roster:
            simulateMatch(team[0],team[2])
        time.sleep(2)
        round += 1

    # Goodbye message
    standings = playerStandings()
    winner = standings[0][1]


    print '''
    \t         ___________
    \t        '._==_==_=_.'         ''' +  winner + ''' Wins!
    \t        .-\:      /-.
    \t       | (|:.     |) |
    \t        '-|:.     |-'
    \t          \::.    /
    \t           '::. .'
    \t             ) (
    \t           _.' '._
    \t          `"""""""`
    '''
    print "\n\tCongratulations " + winner + ", you are the " + game_type + " champion!\n"
    print "\n\tThanks for coming out the the annual " + game_type + " challenge!\n\n\n\n\n"
